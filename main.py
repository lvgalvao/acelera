import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Jornada de Dados",
    page_icon="🚀",
    layout="wide"
)

# CSS personalizado para tema amarelo/preto
st.markdown("""
<style>
    /* Tema principal - fundo escuro com pontos amarelos */
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #1a1a1a 50%, #000000 100%);
        background-image: radial-gradient(circle at 20% 20%, rgba(255, 193, 7, 0.1) 0%, transparent 50%),
                         radial-gradient(circle at 80% 80%, rgba(255, 193, 7, 0.1) 0%, transparent 50%);
        color: white;
    }
    
    /* Título principal */
    .main .block-container h1 {
        color: #FFC107;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        margin-bottom: 0.5rem;
    }
    
    /* Subtítulo */
    .main .block-container p {
        color: white;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    /* Cards das opções */
    .option-card {
        background: linear-gradient(145deg, #1a1a1a, #2d2d2d);
        border: 2px solid #FFC107;
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        margin: 10px 0;
        box-shadow: 0 8px 32px rgba(255, 193, 7, 0.2);
        transition: all 0.3s ease;
    }
    
    .option-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(255, 193, 7, 0.3);
        border-color: #FFD700;
    }
    
    .option-card h3 {
        color: #FFC107;
        margin-top: 0;
        font-size: 1.5rem;
        font-weight: bold;
    }
    
    .option-card p {
        color: #e0e0e0;
        margin-bottom: 0;
    }
    
    /* Botões */
    .stButton > button {
        background: linear-gradient(45deg, #FFC107, #FFD700);
        color: #000000;
        border: none;
        border-radius: 25px;
        font-weight: bold;
        font-size: 1.1rem;
        padding: 0.75rem 2rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 193, 7, 0.3);
    }
    
    .stButton > button:hover {
        background: linear-gradient(45deg, #FFD700, #FFC107);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 193, 7, 0.4);
    }
    
    /* Subheader */
    .main .block-container h2 {
        color: #FFC107;
        text-align: center;
        font-size: 2rem;
        margin: 2rem 0 1rem 0;
    }
    
    /* Info box */
    .stInfo {
        background: linear-gradient(145deg, #1a1a1a, #2d2d2d);
        border: 1px solid #FFC107;
        border-radius: 10px;
    }
    
    /* Footer */
    .footer {
        background: linear-gradient(145deg, #1a1a1a, #2d2d2d);
        border-top: 2px solid #FFC107;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        margin-top: 2rem;
    }
    
    .footer p {
        color: #FFC107;
        font-size: 1.1rem;
        font-weight: bold;
        margin: 0;
    }
    
    /* Divisor */
    hr {
        border: 1px solid #FFC107;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.title("🚀 Jornada de Dados")
st.markdown("**Seja fluente em Dados, Python, SQL e Cloud em um só lugar**")


st.markdown("---")

# Opções de navegação
st.subheader("🎯 Escolha uma opção:")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="option-card">
        <h3>📚 Explorar Trilhas</h3>
        <p>Veja todas as trilhas disponíveis e explore os módulos de cada uma.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("📚 Ver Trilhas", type="primary", width='stretch'):
        st.switch_page("pages/1_📚_Trilhas.py")

with col2:
    st.markdown("""
    <div class="option-card">
        <h3>🎯 Questionário</h3>
        <p>Descubra qual trilha é ideal para você baseado no seu perfil.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🎯 Fazer Questionário", type="secondary", width='stretch'):
        st.switch_page("pages/2_🎯_Questionário.py")

st.markdown("---")

# Informações adicionais
st.info("💡 **Dica:** Se você não tem certeza de qual trilha escolher, recomendamos começar com o questionário para uma orientação personalizada!")

# Footer
st.markdown("---")
st.markdown("""
<div class="footer">
    <p>🚀 Jornada de Dados - Transformando carreiras em dados</p>
</div>
""", unsafe_allow_html=True)
