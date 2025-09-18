import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Questionário - Jornada de Dados",
    page_icon="🎯",
    layout="wide"
)

# Título principal
st.title("🎯 Questionário de Orientação")
st.markdown("**Descubra qual trilha é ideal para você!**")
st.markdown("---")

# Dados das trilhas (mesmo do app principal)
@st.cache_data
def load_trilhas():
    try:
        df_trilhas = pd.read_csv('data/trilha.csv', sep=';')
        return df_trilhas
    except Exception:
        return None

@st.cache_data
def load_cursos():
    try:
        df_cursos = pd.read_csv('data/cursos.csv', sep=';')
        return df_cursos
    except Exception:
        return None

# Mapeamento das trilhas
TRILHAS_MAP = {
    "n8n": "Trilha de I.A. com n8n",
    "sql": "Trilha de SQL e dbt-core", 
    "python": "Trilha de Python",
    "engenharia_de_dados": "Trilha de Engenharia de Dados + IA",
    "aws": "Trilha de AWS"
}

def calcular_trilha_recomendada(respostas):
    """
    Calcula as 3 trilhas recomendadas baseado nas respostas (1 por mês)
    """
    # Trilhas base por objetivo
    trilhas_base = {
        "migrar_area": ["n8n", "sql", "python", "engenharia_de_dados", "aws"],
        "analista_para_engenheiro": ["n8n", "sql", "python", "engenharia_de_dados", "aws"],
        "engenheiro_para_senior": ["n8n", "sql", "python", "engenharia_de_dados", "aws"]
    }
    
    # Começar com trilhas base do objetivo
    trilhas = trilhas_base[respostas["goal"]].copy()
    
    # Aplicar cortes baseado nas respostas
    
    # Se já sabe ETL (intermediário ou avançado), remover n8n
    if respostas["etl_exp"] in ["avancado", "intermediario"]:
        if "n8n" in trilhas:
            trilhas.remove("n8n")
    
    # Se SQL avançado, remover sql
    if respostas["sql_level"] == "avancado":
        if "sql" in trilhas:
            trilhas.remove("sql")
    
    # Ajustes finos
    de_exp = respostas["de_exp"]
    goal = respostas["goal"]
    
    # Se engenheiro para sênior e já tem experiência em DE
    if goal == "engenheiro_para_senior" and de_exp in ["avancado", "intermediario"]:
        # Priorizar engenharia de dados e AWS
        trilhas = ["engenharia_de_dados", "aws"]
        if "python" not in trilhas:
            trilhas.append("python")
    
    # Sempre retornar exatamente 3 trilhas (1 por mês)
    if len(trilhas) > 3:
        trilhas = trilhas[:3]
    elif len(trilhas) < 3:
        # Se tiver menos de 3, adicionar as que faltam
        todas_trilhas = ["n8n", "sql", "python", "engenharia_de_dados", "aws"]
        for trilha in todas_trilhas:
            if trilha not in trilhas and len(trilhas) < 3:
                trilhas.append(trilha)
    
    return trilhas

def gerar_plano_estudos(trilhas_recomendadas, df_cursos):
    """
    Gera um plano de estudos de 3 meses (1 trilha por mês)
    Considerando 2 horas de estudo por dia
    """
    plano = []
    
    for trilha_id in trilhas_recomendadas:
        trilha_nome = TRILHAS_MAP[trilha_id]
        cursos_trilha = df_cursos[df_cursos['Trilha'] == trilha_nome]
        
        # Incluir todos os módulos da trilha
        for _, curso in cursos_trilha.iterrows():
            # Converter minutos para horas
            carga_horas = curso['Carga Horária'] / 60
            
            # Calcular dias necessários (2 horas por dia)
            dias_necessarios = max(1, int(carga_horas / 2))
            
            plano.append({
                'Trilha': trilha_nome,
                'Módulo': curso['Conteúdo'],
                'Carga Horária (h)': round(carga_horas, 1),
                'Dias Necessários': dias_necessarios,
                'Objetivo': curso['Objetivo']
            })
    
    return pd.DataFrame(plano)

def main():
    # Carregar dados das trilhas e cursos
    df_trilhas = load_trilhas()
    df_cursos = load_cursos()
    
    if df_trilhas is None or df_cursos is None:
        st.error("Erro ao carregar dados das trilhas ou cursos.")
        return
    
    # Inicializar session state
    if 'respostas' not in st.session_state:
        st.session_state.respostas = {}
    if 'mostrar_resultado' not in st.session_state:
        st.session_state.mostrar_resultado = False
    
    # Formulário de perguntas
    with st.form("questionario_form"):
        st.subheader("📋 Responda as perguntas abaixo:")
        
        # Pergunta 1: Objetivo
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("**1. Qual é o seu objetivo principal?**")
        with col2:
            objetivo = st.selectbox(
                "Selecione seu objetivo:",
                options=[
                    "migrar_area",
                    "analista_para_engenheiro", 
                    "engenheiro_para_senior"
                ],
                format_func=lambda x: {
                    "migrar_area": "Migrar para a área de dados",
                    "analista_para_engenheiro": "Ser promovido de analista para engenheiro de dados",
                    "engenheiro_para_senior": "Evoluir e me especializar na engenharia de dados"
                }[x],
                key="goal"
            )
        
        st.markdown("---")
        
        # Pergunta 2: Automação
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("**2. Você já criou automações (Power Automate/Excel/n8n/Zapier) na prática?**")
        with col2:
            automacao = st.selectbox(
                "Nível de experiência com automação:",
                options=["avancado", "intermediario", "basico", "iniciante"],
                format_func=lambda x: {
                    "avancado": "Avançado - Criei automações complexas com múltiplas integrações e lógica condicional",
                    "intermediario": "Intermediário - Já criei automações funcionais com algumas integrações",
                    "basico": "Básico - Já usei ferramentas de automação, mas sem criar fluxos complexos",
                    "iniciante": "Iniciante - Nunca criei automações ou uso há menos de 3 meses"
                }[x],
                key="automation_exp"
            )
        
        st.markdown("---")
        
        # Pergunta 3: SQL
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("**3. Qual seu nível de SQL?**")
        with col2:
            sql = st.selectbox(
                "Nível de SQL:",
                options=["avancado", "intermediario", "basico", "iniciante"],
                format_func=lambda x: {
                    "avancado": "Avançado - Criar/modificar tabelas, stored procedures, indexes e partitions",
                    "intermediario": "Intermediário - CTEs, Window Functions, subqueries e otimização",
                    "basico": "Básico - SELECT, JOINs, WHERE, GROUP BY, ORDER BY",
                    "iniciante": "Iniciante - Não sei SQL ou estudo há menos de 3 meses"
                }[x],
                key="sql_level"
            )
        
        st.markdown("---")
        
        # Pergunta 4: ETL/Pipelines
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("**4. Você já fez pipeline/ETL do zero?**")
        with col2:
            etl = st.selectbox(
                "Experiência com ETL/Pipelines:",
                options=["avancado", "intermediario", "basico", "iniciante"],
                format_func=lambda x: {
                    "avancado": "Avançado - Criei pipelines completos com orquestração, monitoramento e tratamento de erros",
                    "intermediario": "Intermediário - Já criei pipelines funcionais com algumas transformações",
                    "basico": "Básico - Já trabalhei com componentes de ETL, mas não criei do zero",
                    "iniciante": "Iniciante - Nunca fiz ETL/pipelines ou estudo há menos de 3 meses"
                }[x],
                key="etl_exp"
            )
        
        st.markdown("---")
        
        # Pergunta 5: Python
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("**5. Qual seu nível de Python?**")
        with col2:
            python = st.selectbox(
                "Nível de Python:",
                options=["avancado", "intermediario", "basico", "iniciante"],
                format_func=lambda x: {
                    "avancado": "Avançado - POO, APIs REST, frameworks (FastAPI/Django), testes e deploy",
                    "intermediario": "Intermediário - Funções, classes básicas, bibliotecas (pandas, requests)",
                    "basico": "Básico - Variáveis, loops, condicionais, listas e dicionários",
                    "iniciante": "Iniciante - Não sei Python ou estudo há menos de 3 meses"
                }[x],
                key="python_level"
            )
        
        st.markdown("---")
        
        # Pergunta 6: Engenharia de Dados
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("**6. Você já atuou em projetos reais de Engenharia de Dados?**")
        with col2:
            de = st.selectbox(
                "Experiência em Engenharia de Dados:",
                options=["avancado", "intermediario", "basico", "iniciante"],
                format_func=lambda x: {
                    "avancado": "Avançado - Lidei com arquiteturas complexas, streaming, observabilidade e DevOps",
                    "intermediario": "Intermediário - Já trabalhei em projetos reais com pipelines e infraestrutura",
                    "basico": "Básico - Já tive contato com conceitos de DE, mas sem projetos práticos",
                    "iniciante": "Iniciante - Nunca atuei em projetos de DE ou estudo há menos de 3 meses"
                }[x],
                key="de_exp"
            )
        
        st.markdown("---")
        
        # Pergunta 7: Nuvem
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("**7. Qual sua experiência com nuvem (AWS/Azure/GCP)?**")
        with col2:
            cloud = st.selectbox(
                "Experiência com nuvem:",
                options=["avancado", "intermediario", "basico", "iniciante"],
                format_func=lambda x: {
                    "avancado": "Avançado - Arquiteturas complexas, múltiplos serviços, IaC (Terraform), DevOps",
                    "intermediario": "Intermediário - Já trabalhei com vários serviços e criei soluções funcionais",
                    "basico": "Básico - Conheço conceitos básicos e já usei alguns serviços simples",
                    "iniciante": "Iniciante - Não tenho experiência com nuvem ou estudo há menos de 3 meses"
                }[x],
                key="cloud_exp"
            )
        
        st.markdown("---")
        
        # Botão para processar
        submitted = st.form_submit_button("🎯 Descobrir Minha Trilha", type="primary")
        
        if submitted:
            # Salvar respostas
            st.session_state.respostas = {
                "goal": objetivo,
                "automation_exp": automacao,
                "sql_level": sql,
                "etl_exp": etl,
                "python_level": python,
                "de_exp": de,
                "cloud_exp": cloud
            }
            st.session_state.mostrar_resultado = True
            st.rerun()
    
    # Mostrar resultado
    if st.session_state.mostrar_resultado and st.session_state.respostas:
        st.markdown("---")
        st.markdown("## 🎯 Sua Trilha Recomendada")
        
        # Calcular trilha recomendada
        trilhas_recomendadas = calcular_trilha_recomendada(st.session_state.respostas)
        
        if trilhas_recomendadas:
            st.success("**Com base nas suas respostas, te recomendamos seguir por essas 3 trilhas nos próximos 3 meses:**")
            
            # Gerar plano de estudos
            plano_estudos = gerar_plano_estudos(trilhas_recomendadas, df_cursos)
            
            # Calcular estatísticas do plano
            total_horas = plano_estudos['Carga Horária (h)'].sum()
            total_dias = plano_estudos['Dias Necessários'].sum()
            total_modulos = len(plano_estudos)
            
            # Mostrar resumo do plano
            st.markdown("---")
            st.markdown("### 📅 Plano de Estudos - Próximos 3 Meses")
            st.markdown("**1 trilha por mês (considerando 2 horas de estudo por dia):**")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("📚 Total de Módulos", total_modulos)
            
            with col2:
                st.metric("⏱️ Carga Horária Total", f"{total_horas:.1f}h")
            
            with col3:
                st.metric("📅 Dias Necessários", total_dias)
            
            with col4:
                st.metric("📆 Duração do Plano", "3 meses")
            
            # Botão para download do CSV
            csv_plano = plano_estudos.to_csv(index=False)
            st.download_button(
                label="📥 Baixar Plano de Estudos (CSV)",
                data=csv_plano,
                file_name="plano_estudos_3_meses.csv",
                mime="text/csv",
                type="primary"
            )
            
            # Mostrar tabela do plano de estudos
            st.markdown("---")
            st.markdown("### 📋 Detalhamento do Plano de Estudos")
            
            # Agrupar por trilha para melhor visualização
            for trilha_id in trilhas_recomendadas:
                trilha_nome = TRILHAS_MAP[trilha_id]
                modulos_trilha = plano_estudos[plano_estudos['Trilha'] == trilha_nome]
                
                if not modulos_trilha.empty:
                    with st.expander(f"📚 {trilha_nome} (1 mês)", expanded=False):
                        # Mostrar tabela dos módulos
                        st.dataframe(
                            modulos_trilha[['Módulo', 'Carga Horária (h)', 'Dias Necessários', 'Objetivo']],
                            use_container_width=True,
                            height=300
                        )
                        
                        # Estatísticas da trilha
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Módulos", len(modulos_trilha))
                        with col2:
                            st.metric("Horas", f"{modulos_trilha['Carga Horária (h)'].sum():.1f}h")
                        with col3:
                            st.metric("Dias", modulos_trilha['Dias Necessários'].sum())
            
            # Mostrar cada trilha recomendada
            for i, trilha_id in enumerate(trilhas_recomendadas, 1):
                trilha_nome = TRILHAS_MAP[trilha_id]
                
                # Buscar descrição da trilha
                descricao = df_trilhas[df_trilhas['trilha'] == trilha_nome]['detalhe'].iloc[0]
                
                with st.expander(f"📚 {i}. {trilha_nome}", expanded=True):
                    st.markdown(f"**Descrição:** {descricao}")
                    
                    # Adicionar informações específicas baseadas no nível
                    respostas = st.session_state.respostas
                    
                    if trilha_id == "python" and respostas["python_level"] in ["avancado", "intermediario"]:
                        st.info("💡 **Dica:** Com seu nível em Python, você pode focar nos módulos mais avançados da trilha!")
                    
                    if trilha_id == "aws" and respostas["cloud_exp"] in ["avancado", "intermediario"]:
                        st.info("💡 **Dica:** Com sua experiência em nuvem, você pode pular os módulos básicos e focar nos avançados!")
                    
                    if trilha_id == "engenharia_de_dados" and respostas["goal"] == "engenheiro_para_senior":
                        st.info("💡 **Dica:** Esta trilha é perfeita para sua evolução para sênior! Foque em streaming, Terraform, K8s e observabilidade.")
                    
                    if trilha_id == "sql" and respostas["sql_level"] in ["avancado", "intermediario"]:
                        st.info("💡 **Dica:** Com seu conhecimento em SQL, foque nos módulos de dbt e otimização avançada!")
                    
                    if trilha_id == "n8n" and respostas["automation_exp"] in ["avancado", "intermediario"]:
                        st.info("💡 **Dica:** Com sua experiência em automação, foque nos projetos avançados e integrações complexas!")
        else:
            st.warning("Não foi possível determinar uma trilha específica. Considere entrar em contato para uma orientação personalizada.")
        
        # Mostrar resumo das respostas
        st.markdown("---")
        st.markdown("### 📊 Resumo das suas respostas:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"**Objetivo:** {st.session_state.respostas['goal']}")
            st.markdown(f"**Automação:** {st.session_state.respostas['automation_exp']}")
            st.markdown(f"**SQL:** {st.session_state.respostas['sql_level']}")
            st.markdown(f"**ETL/Pipelines:** {st.session_state.respostas['etl_exp']}")
        
        with col2:
            st.markdown(f"**Python:** {st.session_state.respostas['python_level']}")
            st.markdown(f"**Engenharia de Dados:** {st.session_state.respostas['de_exp']}")
            st.markdown(f"**Nuvem:** {st.session_state.respostas['cloud_exp']}")
        
        # Botão para refazer
        if st.button("🔄 Refazer Questionário"):
            st.session_state.mostrar_resultado = False
            st.session_state.respostas = {}
            st.rerun()

if __name__ == "__main__":
    main()
