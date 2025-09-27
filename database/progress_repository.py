# database/progress_repository.py

import sqlite3
import pandas as pd
import os
import bcrypt
from typing import Tuple, Optional

class ProgressRepository:
    """
    Repositório para gerenciar o progresso dos alunos no banco de dados SQLite.
    """
    
    def __init__(self, db_path: str = 'data/progresso_alunos.db'):
        """Inicializa o repositório e a conexão com o banco."""
        self.db_path = db_path
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self._create_tables()

    def _create_tables(self):
        """Cria as tabelas do banco de dados se elas não existirem."""
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS aluno_identificacao (
            "id" INTEGER PRIMARY KEY AUTOINCREMENT,
            "email" TEXT UNIQUE NOT NULL,
            "senha_hash" TEXT NOT NULL
        )''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS plano_estudos (
            "id" INTEGER PRIMARY KEY AUTOINCREMENT,
            "aluno_id" INTEGER NOT NULL,
            "Trilha" TEXT, "Módulo" TEXT, "Carga Horária (h)" REAL,
            "Dias Necessários" TEXT, "Objetivo" TEXT,
            "aula_concluida" BOOLEAN DEFAULT FALSE,
            FOREIGN KEY ("aluno_id") REFERENCES "aluno_identificacao"("id")
        )''')
        self.conn.commit()

    @staticmethod
    def _hash_password(password: str) -> str:
        """Gera um hash seguro da senha (método estático)."""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def _check_password(hashed_password: str, plain_password: str) -> bool:
        """Verifica se a senha fornecida corresponde ao hash (método estático)."""
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

    def register_user(self, email: str, password: str) -> Tuple[bool, str]:
        """Registra um novo usuário."""
        if len(password) < 8:
            return False, "A senha deve ter no mínimo 8 caracteres."
        
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT id FROM aluno_identificacao WHERE email = ?", (email,))
            if cursor.fetchone():
                return False, "Este e-mail já está cadastrado."
            
            senha_hash = self._hash_password(password)
            cursor.execute("INSERT INTO aluno_identificacao (email, senha_hash) VALUES (?, ?)", (email, senha_hash))
            self.conn.commit()
            return True, "Usuário registrado com sucesso!"
        except sqlite3.IntegrityError:
            return False, "Este e-mail já está cadastrado."
        except Exception as e:
            return False, f"Erro inesperado: {e}"

    def authenticate_user(self, email: str, password: str) -> Optional[int]:
        """Autentica um usuário e retorna seu ID."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, senha_hash FROM aluno_identificacao WHERE email = ?", (email,))
        user_data = cursor.fetchone()
        
        if user_data:
            user_id, senha_hash = user_data
            if self._check_password(senha_hash, password):
                return user_id
        return None

    def get_user_id(self, email: str) -> Optional[int]:
        """Busca o ID de um usuário pelo seu email."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT id FROM aluno_identificacao WHERE email = ?", (email,))
        result = cursor.fetchone()
        return result[0] if result else None

    def load_plan_for_user(self, user_id: int) -> pd.DataFrame:
        """Carrega o plano de estudos para um ID de usuário específico."""
        query = "SELECT * FROM plano_estudos WHERE aluno_id = ?"
        return pd.read_sql_query(query, self.conn, params=(user_id,))

    def save_plan_from_csv(self, df_csv: pd.DataFrame, user_id: int):
        """Salva um novo plano de estudos para um usuário."""
        colunas_esperadas = ["Trilha", "Módulo", "Carga Horária (h)", "Dias Necessários", "Objetivo"]
        df_filtrado = df_csv[colunas_esperadas].copy()
        df_filtrado['aluno_id'] = user_id
        
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM plano_estudos WHERE aluno_id = ?", (user_id,))
        df_filtrado.to_sql('plano_estudos', self.conn, if_exists='append', index=False)
        self.conn.commit()

    def update_aula_status(self, item_id: int, novo_status: bool, user_id: int):
        """Atualiza o status de uma aula para um usuário específico."""
        cursor = self.conn.cursor()
        query = 'UPDATE plano_estudos SET "aula_concluida" = ? WHERE "id" = ? AND "aluno_id" = ?'
        cursor.execute(query, (novo_status, item_id, user_id))
        self.conn.commit()

    def close(self):
        """Fecha a conexão com o banco de dados."""
        if self.conn:
            self.conn.close()