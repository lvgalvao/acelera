import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
from typing import Optional, Dict, Any, List
import streamlit as st

# Carregar variáveis de ambiente
load_dotenv()

class PostgreSQLClient:
    """
    Cliente para conexão com PostgreSQL (Supabase)
    """
    
    def __init__(self):
        self.connection: Optional[psycopg2.extensions.connection] = None
        self.cursor: Optional[psycopg2.extensions.cursor] = None
        self._initialize_connection()
    
    def _initialize_connection(self):
        """
        Inicializa a conexão com PostgreSQL
        """
        try:
            # Obter credenciais das variáveis de ambiente
            user = os.getenv("user")
            password = os.getenv("password")
            host = os.getenv("host")
            port = os.getenv("port")
            dbname = os.getenv("dbname")
            
            if not all([user, password, host, port, dbname]):
                raise ValueError("Credenciais do PostgreSQL não encontradas no arquivo .env")
            
            # Conectar ao banco
            self.connection = psycopg2.connect(
                user=user,
                password=password,
                host=host,
                port=port,
                dbname=dbname
            )
            
            # Criar cursor
            self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
            
        except Exception as e:
            st.error(f"Erro ao conectar com PostgreSQL: {str(e)}")
            self.connection = None
            self.cursor = None
    
    def is_connected(self) -> bool:
        """
        Verifica se a conexão com PostgreSQL está ativa
        """
        return self.connection is not None and not self.connection.closed
    
    def test_connection(self) -> bool:
        """
        Testa a conexão com PostgreSQL
        """
        try:
            if not self.is_connected():
                return False
            
            # Tentar fazer uma consulta simples
            self.cursor.execute("SELECT NOW();")
            result = self.cursor.fetchone()
            return True
            
        except Exception as e:
            st.error(f"Erro ao testar conexão: {str(e)}")
            return False
    
    def get_connection(self) -> Optional[psycopg2.extensions.connection]:
        """
        Retorna a conexão PostgreSQL
        """
        return self.connection
    
    def get_cursor(self) -> Optional[psycopg2.extensions.cursor]:
        """
        Retorna o cursor PostgreSQL
        """
        return self.cursor
    
    def close_connection(self):
        """
        Fecha a conexão com o banco
        """
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        except Exception as e:
            st.error(f"Erro ao fechar conexão: {str(e)}")
    
    def __del__(self):
        """
        Destructor para fechar conexão automaticamente
        """
        self.close_connection()
