import streamlit as st
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

def get_postgresql_config():
    """
    Obtém as configurações do PostgreSQL de diferentes fontes
    Prioridade: st.secrets > variáveis de ambiente > session_state
    """
    # Tentar obter do st.secrets primeiro
    try:
        if hasattr(st, 'secrets') and 'postgresql' in st.secrets:
            return {
                'user': st.secrets.postgresql.user,
                'password': st.secrets.postgresql.password,
                'host': st.secrets.postgresql.host,
                'port': st.secrets.postgresql.port,
                'dbname': st.secrets.postgresql.dbname
            }
    except:
        pass
    
    # Tentar obter das variáveis de ambiente
    user = os.getenv('user')
    password = os.getenv('password')
    host = os.getenv('host')
    port = os.getenv('port')
    dbname = os.getenv('dbname')
    
    if all([user, password, host, port, dbname]):
        return {
            'user': user,
            'password': password,
            'host': host,
            'port': port,
            'dbname': dbname
        }
    
    # Tentar obter do session_state (para configuração manual)
    if all(key in st.session_state for key in ['postgres_user', 'postgres_password', 'postgres_host', 'postgres_port', 'postgres_dbname']):
        return {
            'user': st.session_state.postgres_user,
            'password': st.session_state.postgres_password,
            'host': st.session_state.postgres_host,
            'port': st.session_state.postgres_port,
            'dbname': st.session_state.postgres_dbname
        }
    
    return None

def setup_postgresql_credentials():
    """
    Interface para configurar credenciais do PostgreSQL manualmente
    """
    st.sidebar.markdown("### 🔧 Configuração do PostgreSQL")
    
    with st.sidebar.expander("Configurar Credenciais", expanded=False):
        st.markdown("**Configure suas credenciais do PostgreSQL:**")
        
        user = st.text_input(
            "Usuário:",
            value=st.session_state.get('postgres_user', ''),
            help="Ex: postgres.zhyycmjndgewmolilfmx"
        )
        
        password = st.text_input(
            "Senha:",
            value=st.session_state.get('postgres_password', ''),
            type="password",
            help="Sua senha do banco de dados"
        )
        
        host = st.text_input(
            "Host:",
            value=st.session_state.get('postgres_host', ''),
            help="Ex: aws-1-us-east-2.pooler.supabase.com"
        )
        
        port = st.text_input(
            "Porta:",
            value=st.session_state.get('postgres_port', ''),
            help="Ex: 6543"
        )
        
        dbname = st.text_input(
            "Nome do Banco:",
            value=st.session_state.get('postgres_dbname', ''),
            help="Ex: postgres"
        )
        
        if st.button("Salvar Configurações"):
            if all([user, password, host, port, dbname]):
                st.session_state.postgres_user = user
                st.session_state.postgres_password = password
                st.session_state.postgres_host = host
                st.session_state.postgres_port = port
                st.session_state.postgres_dbname = dbname
                st.success("✅ Credenciais salvas!")
                st.rerun()
            else:
                st.error("❌ Preencha todos os campos!")
        
        st.markdown("---")
        st.markdown("**Como obter as credenciais:**")
        st.markdown("""
        1. Acesse [supabase.com](https://supabase.com)
        2. Vá em **Settings > Database**
        3. Copie as informações de conexão
        4. Use o **Connection Pooling** para melhor performance
        """)
