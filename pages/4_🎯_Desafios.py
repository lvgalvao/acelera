import streamlit as st
import os

# Configuração da página
st.set_page_config(
    page_title="Desafios Técnicos",
    page_icon="🎯",
    layout="wide"
)

# Forçar tema light
st.markdown("""
<style>
    .stApp {
        color-scheme: light;
    }
    .stApp > header {
        background-color: transparent;
    }
    .stApp > div {
        background-color: #ffffff;
    }
    /* Força o tema light em todos os componentes */
    .stSelectbox > div > div {
        background-color: #ffffff;
        color: #262730;
    }
    .stTextInput > div > div > input {
        background-color: #ffffff;
        color: #262730;
    }
    .stTextArea > div > div > textarea {
        background-color: #ffffff;
        color: #262730;
    }
    .stButton > button {
        background-color: #ffffff;
        color: #262730;
        border: 1px solid #cccccc;
    }
    .stButton > button:hover {
        background-color: #f0f2f6;
        border-color: #1f77b4;
    }
    .stDataFrame {
        background-color: #ffffff;
    }
    .stExpander {
        background-color: #ffffff;
        border: 1px solid #cccccc;
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.title("🎯 Desafios Técnicos das Trilhas")
st.markdown("---")

# Dados dos desafios
desafios_data = {
    "Python": {
        "emoji": "🐍",
        "titulo": "Validação de Dados e Cálculo de Bônus",
        "arquivo": "desafios/python/desafio_01.md",
        "descricao": "Validação de dados de funcionários, cálculo de bônus com regras específicas e geração de relatórios em CSV e JSON.",
        "topics": ["Validação de dados", "Cálculo de bônus", "Geração de relatórios", "CSV/JSON"]
    },
    "SQL": {
        "emoji": "🗄️",
        "titulo": "Funções de Ranking (ROW_NUMBER, RANK e DENSE_RANK)",
        "arquivo": "desafios/sql/desafio_01.md",
        "descricao": "Análise de atividade de e-mails, comparação entre funções de ranking e problema clássico de entrevistas técnicas.",
        "topics": ["Funções de janela", "Ranking", "Entrevistas técnicas", "Análise de dados"]
    },
    "AWS": {
        "emoji": "☁️",
        "titulo": "Streamlit no EC2 com Kaggle + S3",
        "arquivo": "desafios/aws/desafio_01.md",
        "descricao": "Dashboard Streamlit em instância EC2, integração com datasets do Kaggle e armazenamento e leitura de dados no S3.",
        "topics": ["EC2", "S3", "Streamlit", "Kaggle", "Cloud Computing"]
    },
    "Engenharia de Dados": {
        "emoji": "🔧",
        "titulo": "Docker + Airflow (ETL Bitcoin)",
        "arquivo": "desafios/engenharia/desafio_01.md",
        "descricao": "Pipeline ETL com Airflow em Docker, coleta de dados da API Coinbase e agendamento e persistência de dados.",
        "topics": ["Docker", "Airflow", "ETL", "APIs", "Orquestração"]
    },
    "n8n": {
        "emoji": "🤖",
        "titulo": "Agente Financeiro (Telegram + Google Sheets + ChatGPT)",
        "arquivo": "desafios/n8n/desafio_01.md",
        "descricao": "Bot Telegram para controle financeiro, integração com Google Sheets e classificação automática de intenções com IA.",
        "topics": ["Automação", "Telegram", "Google Sheets", "IA", "ChatGPT"]
    }
}

# Função para ler o conteúdo do arquivo markdown
@st.cache_data
def read_desafio_content(arquivo_path):
    try:
        if os.path.exists(arquivo_path):
            with open(arquivo_path, 'r', encoding='utf-8') as file:
                return file.read()
        else:
            return "Arquivo não encontrado."
    except Exception as e:
        return f"Erro ao ler o arquivo: {e}"

# Criar duas colunas
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🎯 Selecione um Desafio")
    
    # Criar selectbox com os desafios
    desafio_selecionado = st.selectbox(
        "Escolha uma trilha:",
        options=list(desafios_data.keys()),
        index=0,
        help="Selecione uma trilha para ver o desafio técnico"
    )

with col2:
    st.subheader("📖 Informações do Desafio")
    
    desafio_info = desafios_data[desafio_selecionado]
    
    # Exibir informações do desafio em um container estilizado
    st.markdown(
        f"""
        <div style="
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #1f77b4;
            margin: 10px 0;
        ">
            <h4 style="color: #1f77b4; margin-top: 0;">
                {desafio_info['emoji']} {desafio_selecionado} - {desafio_info['titulo']}
            </h4>
            <p style="text-align: justify; line-height: 1.6; margin-bottom: 15px;">
                {desafio_info['descricao']}
            </p>
            <div style="margin-top: 15px;">
                <strong>📋 Tópicos abordados:</strong><br>
                {', '.join([f'<span style="background-color: #e1f5fe; padding: 2px 8px; border-radius: 12px; font-size: 0.9em; margin-right: 5px; display: inline-block; margin-bottom: 5px;">{topic}</span>' for topic in desafio_info['topics']])}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Seção do conteúdo do desafio
st.markdown("---")
st.subheader("📋 Conteúdo do Desafio")

# Ler e exibir o conteúdo do arquivo markdown
conteudo_desafio = read_desafio_content(desafio_info['arquivo'])

if conteudo_desafio and conteudo_desafio != "Arquivo não encontrado.":
    # Exibir o conteúdo em um expander
    with st.expander(f"📖 Ver desafio completo: {desafio_info['titulo']}", expanded=True):
        st.markdown(conteudo_desafio)
    
    # Botão para download do arquivo
    st.download_button(
        label=f"📥 Baixar desafio {desafio_selecionado} (MD)",
        data=conteudo_desafio,
        file_name=f"desafio_{desafio_selecionado.lower().replace(' ', '_')}.md",
        mime="text/markdown"
    )
else:
    st.error(f"⚠️ Não foi possível carregar o conteúdo do desafio {desafio_selecionado}")

# Seção de estatísticas
st.markdown("---")
st.subheader("📊 Estatísticas dos Desafios")

col_stats1, col_stats2, col_stats3 = st.columns(3)

with col_stats1:
    st.metric("🎯 Total de Desafios", len(desafios_data))

with col_stats2:
    total_topics = sum(len(desafio['topics']) for desafio in desafios_data.values())
    st.metric("📚 Tópicos Abordados", total_topics)

with col_stats3:
    st.metric("🚀 Trilhas Disponíveis", len(desafios_data))

# Seção de resumo
st.markdown("---")
st.subheader("🎯 Resumo dos Desafios")

# Criar um resumo em formato de cards
for trilha, info in desafios_data.items():
    with st.expander(f"{info['emoji']} {trilha}: {info['titulo']}", expanded=False):
        col_res1, col_res2 = st.columns([2, 1])
        
        with col_res1:
            st.write(f"**Descrição:** {info['descricao']}")
            st.write(f"**Arquivo:** `{info['arquivo']}`")
        
        with col_res2:
            st.write("**Tópicos:**")
            for topic in info['topics']:
                st.write(f"• {topic}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #666; font-size: 0.9em;">
        💡 <strong>Dica:</strong> Complete os desafios na ordem sugerida para maximizar seu aprendizado!
    </div>
    """,
    unsafe_allow_html=True
)
