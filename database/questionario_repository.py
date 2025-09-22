from datetime import datetime
from typing import Dict, Any, List, Optional
import streamlit as st
import json
from .postgresql_client import PostgreSQLClient

class QuestionarioRepository:
    """
    Repositório para gerenciar respostas do questionário no PostgreSQL
    """
    
    def __init__(self):
        self.postgres_client = PostgreSQLClient()
        self.table_name = "respostas_questionario"
    
    def salvar_resposta(self, respostas: Dict[str, Any], trilhas_recomendadas: List[str], trilhas_nomes: List[str]) -> bool:
        """
        Salva uma resposta do questionário no banco de dados
        
        Args:
            respostas: Dicionário com as respostas do questionário
            trilhas_recomendadas: Lista com os IDs das trilhas recomendadas
            trilhas_nomes: Lista com os nomes das trilhas recomendadas
            
        Returns:
            bool: True se salvou com sucesso, False caso contrário
        """
        try:
            if not self.postgres_client.is_connected():
                st.error("Não foi possível conectar com o banco de dados")
                return False
            
            cursor = self.postgres_client.get_cursor()
            connection = self.postgres_client.get_connection()
            
            # Preparar dados para inserção
            timestamp = datetime.now().isoformat()
            respostas_json = json.dumps(respostas)
            trilhas_recomendadas_json = json.dumps(trilhas_recomendadas)
            trilhas_nomes_json = json.dumps(trilhas_nomes)
            
            # Query SQL para inserção
            query = """
                INSERT INTO respostas_questionario 
                (timestamp, respostas, trilhas_recomendadas, trilhas_nomes, created_at)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id;
            """
            
            # Executar inserção
            cursor.execute(query, (
                timestamp,
                respostas_json,
                trilhas_recomendadas_json,
                trilhas_nomes_json,
                timestamp
            ))
            
            # Confirmar transação
            connection.commit()
            
            # Verificar se inseriu
            result = cursor.fetchone()
            if result:
                st.success("✅ Resposta salva com sucesso no banco de dados!")
                return True
            else:
                st.error("Erro ao salvar resposta no banco de dados")
                return False
                
        except Exception as e:
            st.error(f"Erro ao salvar resposta: {str(e)}")
            if connection:
                connection.rollback()
            return False
    
    def buscar_todas_respostas(self) -> List[Dict[str, Any]]:
        """
        Busca todas as respostas do questionário
        
        Returns:
            List[Dict]: Lista com todas as respostas
        """
        try:
            if not self.postgres_client.is_connected():
                st.error("Não foi possível conectar com o banco de dados")
                return []
            
            cursor = self.postgres_client.get_cursor()
            
            query = """
                SELECT * FROM respostas_questionario 
                ORDER BY created_at DESC;
            """
            
            cursor.execute(query)
            results = cursor.fetchall()
            
            # Converter para lista de dicionários
            respostas = []
            for row in results:
                respostas.append(dict(row))
            
            return respostas
            
        except Exception as e:
            st.error(f"Erro ao buscar respostas: {str(e)}")
            return []
    
    def buscar_resposta_por_id(self, resposta_id: int) -> Optional[Dict[str, Any]]:
        """
        Busca uma resposta específica por ID
        
        Args:
            resposta_id: ID da resposta
            
        Returns:
            Dict ou None: Dados da resposta ou None se não encontrada
        """
        try:
            if not self.postgres_client.is_connected():
                st.error("Não foi possível conectar com o banco de dados")
                return None
            
            cursor = self.postgres_client.get_cursor()
            
            query = """
                SELECT * FROM respostas_questionario 
                WHERE id = %s;
            """
            
            cursor.execute(query, (resposta_id,))
            result = cursor.fetchone()
            
            return dict(result) if result else None
            
        except Exception as e:
            st.error(f"Erro ao buscar resposta por ID: {str(e)}")
            return None
    
    def contar_respostas(self) -> int:
        """
        Conta o total de respostas no banco
        
        Returns:
            int: Número total de respostas
        """
        try:
            if not self.postgres_client.is_connected():
                return 0
            
            cursor = self.postgres_client.get_cursor()
            
            query = "SELECT COUNT(*) FROM respostas_questionario;"
            
            cursor.execute(query)
            result = cursor.fetchone()
            
            return result['count'] if result else 0
            
        except Exception as e:
            st.error(f"Erro ao contar respostas: {str(e)}")
            return 0
    
    def buscar_respostas_por_periodo(self, data_inicio: str, data_fim: str) -> List[Dict[str, Any]]:
        """
        Busca respostas por período
        
        Args:
            data_inicio: Data de início (formato ISO)
            data_fim: Data de fim (formato ISO)
            
        Returns:
            List[Dict]: Lista com respostas do período
        """
        try:
            if not self.postgres_client.is_connected():
                st.error("Não foi possível conectar com o banco de dados")
                return []
            
            cursor = self.postgres_client.get_cursor()
            
            query = """
                SELECT * FROM respostas_questionario 
                WHERE created_at >= %s AND created_at <= %s
                ORDER BY created_at DESC;
            """
            
            cursor.execute(query, (data_inicio, data_fim))
            results = cursor.fetchall()
            
            # Converter para lista de dicionários
            respostas = []
            for row in results:
                respostas.append(dict(row))
            
            return respostas
            
        except Exception as e:
            st.error(f"Erro ao buscar respostas por período: {str(e)}")
            return []
    
    def deletar_resposta(self, resposta_id: int) -> bool:
        """
        Deleta uma resposta específica
        
        Args:
            resposta_id: ID da resposta a ser deletada
            
        Returns:
            bool: True se deletou com sucesso, False caso contrário
        """
        try:
            if not self.postgres_client.is_connected():
                st.error("Não foi possível conectar com o banco de dados")
                return False
            
            cursor = self.postgres_client.get_cursor()
            connection = self.postgres_client.get_connection()
            
            query = "DELETE FROM respostas_questionario WHERE id = %s;"
            
            cursor.execute(query, (resposta_id,))
            connection.commit()
            
            if cursor.rowcount > 0:
                st.success("Resposta deletada com sucesso!")
                return True
            else:
                st.error("Resposta não encontrada")
                return False
                
        except Exception as e:
            st.error(f"Erro ao deletar resposta: {str(e)}")
            if connection:
                connection.rollback()
            return False
