import streamlit as st
import pandas as pd
import sys
import os

# Adicionar o diretório raiz ao path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configuração da página
st.set_page_config(
    page_title="Spark e Databricks - Jornada de Dados",
    page_icon="⚡",
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
    .stMetric {
        background-color: #ffffff;
    }
    .stInfo {
        background-color: #e6f3ff;
        border: 1px solid #1f77b4;
    }
    .stSuccess {
        background-color: #e6ffe6;
        border: 1px solid #28a745;
    }
    .stWarning {
        background-color: #fff3cd;
        border: 1px solid #ffc107;
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.title("⚡ Spark e Databricks")
st.markdown("**Plataforma de dados moderna com Spark e Databricks**")
st.info("📅 Início das turmas: 13, 14 e 15 de outubro")
st.markdown("---")

# Dados hardcoded do Spark e Databricks
@st.cache_data
def load_databricks_data():
    dados = [
        {"conteudo": "Introdução ao Databricks e ao Lakehouse", "carga_horaria": 90, "objetivo": "Compreender a visão geral da plataforma e o conceito de Lakehouse.", "certificacao": "Associate ✅"},
        {"conteudo": "Arquitetura de Dados Moderna", "carga_horaria": 90, "objetivo": "Diferenciar Data Lake, Data Warehouse e Lakehouse.", "certificacao": "Associate ✅"},
        {"conteudo": "Configuração do Workspace Databricks", "carga_horaria": 90, "objetivo": "Aprender a criar clusters, gerenciar usuários e permissões.", "certificacao": "Associate ✅"},
        {"conteudo": "Primeiro Notebook no Databricks", "carga_horaria": 90, "objetivo": "Executar PySpark e SQL, integrando notebooks com Git.", "certificacao": "Associate ✅"},
        {"conteudo": "Fundamentos do Spark e PySpark", "carga_horaria": 90, "objetivo": "Entender RDDs, DataFrames e paralelismo.", "certificacao": "Associate ✅"},
        {"conteudo": "Transformações e Ações no Spark", "carga_horaria": 90, "objetivo": "Praticar operações como filter, map, groupBy e join.", "certificacao": "Associate ✅"},
        {"conteudo": "Leitura e Escrita de Dados", "carga_horaria": 90, "objetivo": "Carregar e salvar dados em CSV, JSON, Parquet e Delta Lake.", "certificacao": "Associate ✅"},
        {"conteudo": "SQL no Databricks", "carga_horaria": 90, "objetivo": "Utilizar queries SQL, views e otimizações básicas.", "certificacao": "Associate ✅"},
        {"conteudo": "Ingestão de Dados Batch", "carga_horaria": 90, "objetivo": "Integrar dados de APIs, bancos relacionais e arquivos externos.", "certificacao": "Associate ✅"},
        {"conteudo": "Camadas Bronze, Silver e Gold", "carga_horaria": 90, "objetivo": "Implementar pipelines estruturadas no modelo de camadas.", "certificacao": "Associate ✅"},
        {"conteudo": "Qualidade e Governança de Dados", "carga_horaria": 90, "objetivo": "Aplicar schema enforcement e data quality checks.", "certificacao": "Associate ✅"},
        {"conteudo": "Delta Lake Avançado", "carga_horaria": 90, "objetivo": "Explorar ACID transactions, time travel e otimizações.", "certificacao": "Associate ✅ / Professional ⭐"},
        {"conteudo": "Conceitos de Streaming no Spark", "carga_horaria": 90, "objetivo": "Entender microbatch vs continuous e arquitetura de streaming.", "certificacao": "Associate ✅"},
        {"conteudo": "Structured Streaming com PySpark", "carga_horaria": 90, "objetivo": "Ler dados de Kafka e sockets em tempo real.", "certificacao": "Associate ✅ / Professional ⭐"},
        {"conteudo": "Transformações e Janelas em Streaming", "carga_horaria": 90, "objetivo": "Realizar agregações e aplicar watermarks em fluxos.", "certificacao": "Professional ⭐"},
        {"conteudo": "Integração com Dashboards em Tempo Real", "carga_horaria": 90, "objetivo": "Conectar dados em streaming ao Power BI e Databricks SQL.", "certificacao": "Associate ✅"},
        {"conteudo": "Orquestração com Databricks Workflows", "carga_horaria": 90, "objetivo": "Configurar jobs, triggers e dependências.", "certificacao": "Associate ✅ / Professional ⭐"},
        {"conteudo": "Integração com dbt-core e SQL", "carga_horaria": 90, "objetivo": "Criar modelos versionados e documentados.", "certificacao": "Professional ⭐"},
        {"conteudo": "Infraestrutura como Código no Databricks", "carga_horaria": 90, "objetivo": "Automatizar clusters e permissões com Terraform.", "certificacao": "Professional ⭐"},
        {"conteudo": "Projeto Batch + Streaming", "carga_horaria": 90, "objetivo": "Construir pipeline real unindo ingestão batch e streaming.", "certificacao": "Associate ✅ / Professional ⭐"},
        {"conteudo": "Otimização de Jobs Spark", "carga_horaria": 90, "objetivo": "Aplicar técnicas de particionamento, caching e adaptive execution.", "certificacao": "Professional ⭐"},
        {"conteudo": "Segurança e Governança com Unity Catalog", "carga_horaria": 90, "objetivo": "Configurar permissões, lineage e auditoria.", "certificacao": "Professional ⭐"},
        {"conteudo": "Preparação para Certificação Databricks", "carga_horaria": 90, "objetivo": "Revisar conteúdo oficial e realizar simulados.", "certificacao": "Associate ✅ / Professional ⭐"},
        {"conteudo": "Projeto Final End-to-End", "carga_horaria": 90, "objetivo": "Desenvolver pipeline completo com batch, streaming, dashboards e governança.", "certificacao": "Professional ⭐"},
    ]
    
    return pd.DataFrame(dados)

def main():
    # Carregar dados
    df_databricks = load_databricks_data()
    
    # Informações gerais da trilha
    st.markdown("## 📊 Visão Geral da Trilha")
    
    # Calcular estatísticas (convertendo minutos para horas)
    total_modulos = len(df_databricks)
    total_horas = df_databricks['carga_horaria'].sum() / 60.0
    total_dias = total_horas / 2  # Considerando 2 horas por dia
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📚 Total de Módulos", total_modulos)
    
    with col2:
        st.metric("⏱️ Carga Horária Total", f"{total_horas:.1f}h")
    
    with col3:
        st.metric("📅 Dias de Estudo", f"{total_dias:.0f} dias")
    
    with col4:
        st.metric("📆 Duração Estimada", f"{total_dias/30:.1f} meses")
    
    st.markdown("---")
    
    # Filtros e visualizações
    st.markdown("## 🔍 Explorar Módulos")
    
    # Filtro por certificação
    certificacoes = df_databricks['certificacao'].unique()
    certificacao_selecionada = st.selectbox(
        "Filtrar por Certificação:",
        options=["Todas"] + list(certificacoes),
        help="Selecione uma certificação para filtrar os módulos"
    )
    
    # Aplicar filtro
    if certificacao_selecionada != "Todas":
        df_filtrado = df_databricks[df_databricks['certificacao'] == certificacao_selecionada]
    else:
        df_filtrado = df_databricks
    
    # Mostrar estatísticas do filtro
    if certificacao_selecionada != "Todas":
        st.info(f"📋 Mostrando {len(df_filtrado)} módulos para certificação: **{certificacao_selecionada}**")
    
    # Tabela dos módulos
    st.markdown("### 📚 Módulos da Trilha")
    
    # Preparar dataframe para exibição
    df_display = pd.DataFrame({
        'Módulo': df_filtrado['conteudo'],
        'Carga Horária (h)': df_filtrado['carga_horaria'] / 60.0,
        'Dias Necessários': (df_filtrado['carga_horaria'] / 60.0 / 2.0).round(1),
        'Objetivo': df_filtrado['objetivo'],
        'Certificação': df_filtrado['certificacao'],
    })
    
    st.dataframe(
        df_display,
        height=400,
        use_container_width=True
    )
    
    # Botão para download
    csv_data = df_display.to_csv(index=False)
    st.download_button(
        label="📥 Baixar Módulos (CSV)",
        data=csv_data,
        file_name="modulos_spark_databricks.csv",
        mime="text/csv",
        type="primary"
    )
    
    st.markdown("---")
    
    # Análise por certificação
    st.markdown("## 🏆 Análise por Certificação")
    
    # Contar módulos por certificação
    certificacao_counts = df_databricks['certificacao'].value_counts()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Distribuição de Módulos")
        st.bar_chart(certificacao_counts)
    
    with col2:
        st.markdown("### 📈 Estatísticas por Certificação")
        
        for cert, count in certificacao_counts.items():
            modulos_cert = df_databricks[df_databricks['certificacao'] == cert]
            horas_cert = modulos_cert['carga_horaria'].sum() / 60.0
            dias_cert = horas_cert / 2
            
            with st.expander(f"🏆 {cert} ({count} módulos)"):
                st.metric("Módulos", count)
                st.metric("Horas", f"{horas_cert:.1f}h")
                st.metric("Dias", f"{dias_cert:.0f} dias")
    
    st.markdown("---")
    
    # Roadmap de estudo
    st.markdown("## 🗺️ Roadmap de Estudo Sugerido")
    
    # Dividir em fases baseado na certificação
    associate_modules = df_databricks[df_databricks['certificacao'].str.contains('Associate', na=False)]
    professional_modules = df_databricks[df_databricks['certificacao'].str.contains('Professional', na=False)]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🥉 Fase 1: Associate (Fundamentos)")
        st.markdown(f"**{len(associate_modules)} módulos - {associate_modules['carga_horaria'].sum()/60.0/2:.0f} dias de estudo**")
        
        with st.expander("Ver módulos Associate", expanded=True):
            for idx, row in associate_modules.iterrows():
                st.markdown(f"**{row['conteudo']}**")
                st.markdown(f"⏱️ {row['carga_horaria']/60.0:.1f}h | 🎯 {row['objetivo']}")
                st.markdown("---")
    
    with col2:
        st.markdown("### 🥇 Fase 2: Professional (Avançado)")
        st.markdown(f"**{len(professional_modules)} módulos - {professional_modules['carga_horaria'].sum()/60.0/2:.0f} dias de estudo**")
        
        with st.expander("Ver módulos Professional", expanded=True):
            for idx, row in professional_modules.iterrows():
                st.markdown(f"**{row['conteudo']}**")
                st.markdown(f"⏱️ {row['carga_horaria']/60.0:.1f}h | 🎯 {row['objetivo']}")
                st.markdown("---")
    
    st.markdown("---")
    
    # Dicas e recursos
    st.markdown("## 💡 Dicas e Recursos")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🎯 **Foco Associate**")
        st.markdown("""
        - Domine os fundamentos do Spark
        - Pratique com notebooks Databricks
        - Entenda o conceito de Lakehouse
        - Trabalhe com Delta Lake básico
        """)
    
    with col2:
        st.markdown("### 🚀 **Foco Professional**")
        st.markdown("""
        - Aprofunde em streaming
        - Domine Unity Catalog
        - Automatize com Terraform
        - Otimize performance
        """)
    
    with col3:
        st.markdown("### 📚 **Recursos Úteis**")
        st.markdown("""
        - [Documentação Databricks](https://docs.databricks.com/)
        - [Spark Documentation](https://spark.apache.org/docs/)
        - [Delta Lake Guide](https://delta.io/)
        - [Databricks Academy](https://academy.databricks.com/)
        """)
    
    st.markdown("---")
    
    # Footer
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9em;">
        <p>⚡ Spark e Databricks - Transformando dados em insights</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
