import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Trilhas de Aprendizado",
    page_icon="📚",
    layout="wide"
)

# Título principal
st.title("📚 Trilhas de Aprendizado")
st.markdown("---")

# Carregar os dados do CSV
@st.cache_data
def load_data():
    try:
        # Lê o arquivo CSV com separador ';'
        df_trilhas = pd.read_csv('data/trilha.csv', sep=';')
        df_cursos = pd.read_csv('data/cursos.csv', sep=';')
        return df_trilhas, df_cursos
    except FileNotFoundError as e:
        st.error(f"Arquivo não encontrado: {e}")
        return None, None
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return None, None

# Carregar os dados
df_trilhas, df_cursos = load_data()

if df_trilhas is not None and df_cursos is not None:
    # Criar duas colunas
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🎯 Selecione uma Trilha")
        
        # Criar selectbox com as trilhas
        trilha_selecionada = st.selectbox(
            "Escolha uma trilha:",
            options=df_trilhas['trilha'].tolist(),
            index=0,
            help="Selecione uma trilha para ver sua descrição detalhada"
        )
    
    with col2:
        st.subheader("📖 Descrição da Trilha")
        
        # Filtrar a descrição da trilha selecionada
        descricao = df_trilhas[df_trilhas['trilha'] == trilha_selecionada]['detalhe'].iloc[0]
        
        # Exibir a descrição em um container estilizado
        st.markdown(
            f"""
            <div style="
                background-color: #f0f2f6;
                padding: 20px;
                border-radius: 10px;
                border-left: 5px solid #1f77b4;
                margin: 10px 0;
            ">
                <h4 style="color: #1f77b4; margin-top: 0;">{trilha_selecionada}</h4>
                <p style="text-align: justify; line-height: 1.6; margin-bottom: 0;">
                    {descricao}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Seção dos módulos da trilha selecionada
    st.markdown("---")
    st.subheader("📋 Módulos da Trilha")
    
    # Filtrar os cursos da trilha selecionada
    cursos_trilha = df_cursos[df_cursos['Trilha'] == trilha_selecionada]
    
    if not cursos_trilha.empty:
        # Calcular estatísticas da trilha (convertendo minutos para horas)
        total_minutos = cursos_trilha['Carga Horária'].sum()
        total_horas = total_minutos / 60
        total_modulos = len(cursos_trilha)
        
        # Mostrar estatísticas
        col_stats1, col_stats2, col_stats3 = st.columns(3)
        
        with col_stats1:
            st.metric("📚 Total de Módulos", total_modulos)
        
        with col_stats2:
            st.metric("⏱️ Carga Horária Total", f"{total_horas:.1f}h")
        
        with col_stats3:
            st.metric("📈 Média por Módulo", f"{total_horas/total_modulos:.1f}h")
        
        st.markdown("---")
        
        # Mostrar os módulos em formato de tabela expandida
        for idx, (_, modulo) in enumerate(cursos_trilha.iterrows(), 1):
            with st.expander(f"📖 Módulo {idx}: {modulo['Conteúdo']}", expanded=False):
                col_mod1, col_mod2 = st.columns([3, 1])
                
                with col_mod1:
                    st.write(f"**Objetivo:** {modulo['Objetivo']}")
                
                with col_mod2:
                    duracao_horas = modulo['Carga Horária'] / 60
                    st.write(f"**⏱️ Duração:** {duracao_horas:.1f}h")
        
        # Opção para mostrar todos os módulos em tabela
        st.markdown("---")
        if st.checkbox("📊 Ver todos os módulos em tabela"):
            # Preparar dados para exibição (convertendo minutos para horas)
            tabela_modulos = cursos_trilha[['Conteúdo', 'Carga Horária', 'Objetivo']].copy()
            tabela_modulos['Carga Horária'] = tabela_modulos['Carga Horária'] / 60
            tabela_modulos.columns = ['Módulo', 'Carga Horária (h)', 'Objetivo']
            tabela_modulos.index = range(1, len(tabela_modulos) + 1)
            
            st.dataframe(
                tabela_modulos,
                use_container_width=True,
                height=400
            )
            
            # Botão para download
            csv = tabela_modulos.to_csv(index=True)
            st.download_button(
                label="📥 Baixar lista de módulos (CSV)",
                data=csv,
                file_name=f"modulos_{trilha_selecionada.replace(' ', '_')}.csv",
                mime="text/csv"
            )
    
    else:
        st.warning(f"⚠️ Nenhum módulo encontrado para a trilha '{trilha_selecionada}'")
    
