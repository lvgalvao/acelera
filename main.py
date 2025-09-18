import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Jornada de Dados",
    page_icon="🚀",
    layout="wide"
)

# Título principal
st.title("🚀 Jornada de Dados")
st.markdown("**Seja fluente em Dados, Python, SQL e Cloud em um só lugar**")

# Imagem do acelerador
st.image("img/acelerador.jpg", width=600, caption="Acelera - Seus melhores 90 dias")

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
    
    if st.button("📚 Ver Trilhas", type="primary", use_container_width=True):
        st.switch_page("pages/1_📚_Trilhas.py")

with col2:
    st.markdown("""
    <div style="
        background-color: #f0f2f6;
        padding: 30px;
        border-radius: 10px;
        border-left: 5px solid #ff6b6b;
        text-align: center;
        margin: 10px 0;
    ">
        <h3 style="color: #ff6b6b; margin-top: 0;">🎯 Questionário</h3>
        <p>Descubra qual trilha é ideal para você baseado no seu perfil.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🎯 Fazer Questionário", type="secondary", use_container_width=True):
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
