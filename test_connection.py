#!/usr/bin/env python3
"""
Script para testar a conexão com o banco PostgreSQL
"""

import psycopg2
from dotenv import load_dotenv
import os
import sys

# Adicionar o diretório raiz ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import PostgreSQLClient, QuestionarioRepository

def test_direct_connection():
    """
    Testa conexão direta com psycopg2
    """
    print("🔍 Testando conexão direta com psycopg2...")
    
    # Load environment variables from .env
    load_dotenv()

    # Fetch variables
    USER = os.getenv("user")
    PASSWORD = os.getenv("password")
    HOST = os.getenv("host")
    PORT = os.getenv("port")
    DBNAME = os.getenv("dbname")

    print(f"📋 Configurações:")
    print(f"   User: {USER}")
    print(f"   Host: {HOST}")
    print(f"   Port: {PORT}")
    print(f"   Database: {DBNAME}")
    print(f"   Password: {'*' * len(PASSWORD) if PASSWORD else 'NÃO DEFINIDA'}")

    # Connect to the database
    try:
        connection = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME
        )
        print("✅ Conexão direta bem-sucedida!")
        
        # Create a cursor to execute SQL queries
        cursor = connection.cursor()
        
        # Example query
        cursor.execute("SELECT NOW();")
        result = cursor.fetchone()
        print(f"⏰ Hora atual do servidor: {result[0]}")

        # Test table existence
        cursor.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'respostas_questionario'
            );
        """)
        table_exists = cursor.fetchone()[0]
        
        if table_exists:
            print("✅ Tabela 'respostas_questionario' existe!")
            
            # Count records
            cursor.execute("SELECT COUNT(*) FROM respostas_questionario;")
            count = cursor.fetchone()[0]
            print(f"📊 Total de registros: {count}")
        else:
            print("⚠️  Tabela 'respostas_questionario' não existe!")
            print("💡 Execute o script SQL em database/schema.sql para criar a tabela")

        # Close the cursor and connection
        cursor.close()
        connection.close()
        print("🔒 Conexão fechada.")
        
        return True

    except Exception as e:
        print(f"❌ Falha na conexão direta: {e}")
        return False

def test_client_connection():
    """
    Testa conexão usando PostgreSQLClient
    """
    print("\n🔍 Testando conexão usando PostgreSQLClient...")
    
    try:
        client = PostgreSQLClient()
        
        if client.is_connected():
            print("✅ PostgreSQLClient conectado com sucesso!")
            
            if client.test_connection():
                print("✅ Teste de conexão passou!")
            else:
                print("❌ Teste de conexão falhou!")
                
            client.close_connection()
            return True
        else:
            print("❌ PostgreSQLClient não conseguiu conectar!")
            return False
            
    except Exception as e:
        print(f"❌ Erro no PostgreSQLClient: {e}")
        return False

def test_repository():
    """
    Testa o repositório
    """
    print("\n🔍 Testando QuestionarioRepository...")
    
    try:
        repo = QuestionarioRepository()
        
        if repo.postgres_client.is_connected():
            print("✅ QuestionarioRepository conectado!")
            
            # Test count
            count = repo.contar_respostas()
            print(f"📊 Total de respostas: {count}")
            
            return True
        else:
            print("❌ QuestionarioRepository não conseguiu conectar!")
            return False
            
    except Exception as e:
        print(f"❌ Erro no QuestionarioRepository: {e}")
        return False

def main():
    """
    Função principal de teste
    """
    print("🚀 Iniciando testes de conexão com PostgreSQL...")
    print("=" * 50)
    
    # Verificar se arquivo .env existe
    if not os.path.exists('.env'):
        print("⚠️  Arquivo .env não encontrado!")
        print("💡 Crie um arquivo .env com as credenciais do banco:")
        print("""
user=postgres.zhyycmjndgewmolilfmx
password=[YOUR-PASSWORD]
host=aws-1-us-east-2.pooler.supabase.com
port=6543
dbname=postgres
        """)
        return
    
    # Executar testes
    tests = [
        ("Conexão Direta", test_direct_connection),
        ("PostgreSQLClient", test_client_connection),
        ("QuestionarioRepository", test_repository)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Erro inesperado em {test_name}: {e}")
            results.append((test_name, False))
    
    # Resumo dos resultados
    print("\n" + "=" * 50)
    print("📋 RESUMO DOS TESTES:")
    print("=" * 50)
    
    for test_name, result in results:
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"{test_name}: {status}")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"\n🎯 Resultado: {passed}/{total} testes passaram")
    
    if passed == total:
        print("🎉 Todos os testes passaram! A aplicação está pronta para uso.")
    else:
        print("⚠️  Alguns testes falharam. Verifique as configurações.")

if __name__ == "__main__":
    main()
