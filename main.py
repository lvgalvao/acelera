import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Jornada de Dados",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
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
</style>
""", unsafe_allow_html=True)


# Título principal
st.title("Jornada de Dados")
st.markdown("**Acelera - Seus melhores 90 dias**")


st.markdown("---")

# Opções de navegação
st.subheader("🎯 Escolha uma opção:")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="
        background-color: #f0f2f6;
        padding: 30px;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        text-align: center;
        margin: 10px 0;
    ">
        <h3 style="color: #1f77b4; margin-top: 0;">📚 Explorar Trilhas</h3>
        <p>Veja todas as trilhas disponíveis e explore os módulos de cada uma.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("📚 Ver Trilhas", type="secondary"):
        st.switch_page("pages/1_📚_Trilhas.py")

with col2:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #fff5f5 0%, #ffe6e6 100%);
        padding: 35px;
        border-radius: 15px;
        border: 3px solid #ff6b6b;
        text-align: center;
        margin: 10px 0;
        box-shadow: 0 8px 25px rgba(255, 107, 107, 0.2);
        transform: scale(1.02);
    ">
        <h3 style="color: #ff6b6b; margin-top: 0; font-size: 1.6rem; font-weight: bold;">🎯 Questionário</h3>
        <p style="font-size: 1.1rem; font-weight: 500;">Descubra qual trilha é ideal para você baseado no seu perfil.</p>
        <p style="color: #ff6b6b; font-weight: bold; margin-top: 10px;">✨ Recomendado para iniciantes</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🎯 Fazer Questionário", type="primary"):
        st.switch_page("pages/2_🎯_Questionário.py")

st.markdown("---")

# Informações adicionais
st.info("💡 **Dica:** Se você não tem certeza de qual trilha escolher, recomendamos começar com o questionário para uma orientação personalizada!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9em;">
    <p>🚀 Jornada de Dados - Transformando carreiras em dados</p>
</div>
""", unsafe_allow_html=True)
