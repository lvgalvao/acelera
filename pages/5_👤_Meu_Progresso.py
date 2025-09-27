import streamlit as st
import pandas as pd
from database import ProgressRepository

st.set_page_config(page_title="Meu Progresso", layout="wide", initial_sidebar_state="collapsed")

repo = ProgressRepository() 

# --- Inicialização da Sessão ---
if 'logged_in_user_id' not in st.session_state:
    st.session_state.logged_in_user_id = None
if 'auth_mode' not in st.session_state:
    st.session_state.auth_mode = 'login' 
# --- Flags para disparar a celebração na próxima recarga ---
if 'celebrate_trilha_nome' not in st.session_state:
    st.session_state.celebrate_trilha_nome = None
if 'celebrate_plano_completo' not in st.session_state:
    st.session_state.celebrate_plano_completo = False


# --- Função auxiliar para não repetir código ---
def calcular_progresso(df):
    """Calcula o progresso geral e por trilha de um DataFrame de plano."""
    if df.empty:
        return 0, pd.DataFrame(columns=['Trilha', 'progresso_%'])
        
    total_aulas = len(df)
    aulas_concluidas = int(df['aula_concluida'].sum())
    progresso_geral = (aulas_concluidas / total_aulas) * 100 if total_aulas > 0 else 0
    
    prog_trilha = df.groupby('Trilha').agg(
        total_aulas=('Módulo', 'count'), 
        aulas_concluidas=('aula_concluida', 'sum')
    ).reset_index()
    prog_trilha['progresso_%'] = prog_trilha.apply(
        lambda row: (row['aulas_concluidas'] / row['total_aulas'] * 100) if row['total_aulas'] > 0 else 0, 
        axis=1
    ).round(1)
    
    return progresso_geral, prog_trilha


# ===================================================================
# PARTE 1: TELA DE AUTENTICAÇÃO
# ===================================================================
if st.session_state.logged_in_user_id is None:
    st.title("👤 Acesso ao Dashboard de Progresso")
    if st.session_state.auth_mode == 'login':
        st.info("Entre para continuar de onde parou.")
        with st.form("login_form"):
            email = st.text_input("E-mail")
            password = st.text_input("Senha", type="password")
            if st.form_submit_button("▶️ Entrar"):
                user_id = repo.authenticate_user(email, password)
                if user_id:
                    st.session_state.logged_in_user_id = user_id
                    st.rerun()
                else:
                    st.error("E-mail ou senha inválidos.")
        if st.button("Não tenho acesso, criar um agora"):
            st.session_state.auth_mode = 'register'
            st.rerun()
    elif st.session_state.auth_mode == 'register':
        st.info("Crie seu acesso e carregue seu plano de estudos para começar.")
        with st.form("register_form"):
            st.markdown("##### Crie seu acesso")
            email_reg = st.text_input("Seu E-mail")
            password_reg = st.text_input("Crie uma Senha (mín. 8 caracteres)", type="password")
            st.markdown("##### Carregue seu plano")
            uploaded_file = st.file_uploader("Arquivo 'plano_de_estudos.csv':")
            if st.form_submit_button("➕ Criar Acesso e Salvar Plano"):
                if not all([email_reg, password_reg, uploaded_file]):
                    st.warning("Por favor, preencha todos os campos e carregue o arquivo.")
                else:
                    success, message = repo.register_user(email_reg, password_reg)
                    if success:
                        user_id = repo.get_user_id(email_reg)
                        if user_id:
                            df_csv = pd.read_csv(uploaded_file)
                            repo.save_plan_from_csv(df_csv, user_id)
                            st.success("Conta criada e plano salvo com sucesso! Faça o login para continuar.")
                            st.session_state.auth_mode = 'login'
                            st.rerun()
                        else: st.error("Erro ao encontrar usuário recém-criado.")
                    else: st.error(message)
        if st.button("Já tenho acesso, fazer login"):
            st.session_state.auth_mode = 'login'
            st.rerun()

# =====================================================================
# PARTE 2: DASHBOARD (Se estiver logado)
# =====================================================================
else:
    user_id = st.session_state.logged_in_user_id
    st.title("📊 Dashboard do Plano de Estudos")

    if st.button("Sair da Conta (Logout)"):
        st.session_state.logged_in_user_id = None
        st.rerun()

    df_plano = repo.load_plan_for_user(user_id)
    
    if df_plano.empty:
        st.warning("Seu plano de estudos está vazio!")
        uploaded_file = st.file_uploader("Carregar 'plano_de_estudos.csv':", type="csv")
        if uploaded_file is not None:
            df_csv = pd.read_csv(uploaded_file)
            repo.save_plan_from_csv(df_csv, user_id)
            st.success("Seu plano foi salvo! A página será recarregada.")
            st.rerun()
    else:
        # --- Dispara as animações se as flags estiverem ativas ---
        if st.session_state.celebrate_plano_completo:
            st.snow()
            st.success("🎉 PARABÉNS! Você concluiu toda a sua jornada! 🎉")
            st.session_state.celebrate_plano_completo = False # Reseta a flag

        if st.session_state.celebrate_trilha_nome:
            st.balloons()
            st.info(f"🚀 Boa! Você completou a trilha: **{st.session_state.celebrate_trilha_nome}**")
            st.session_state.celebrate_trilha_nome = None # Reseta a flag

        df_plano['aula_concluida'] = df_plano['aula_concluida'].fillna(False).astype(bool)
        df_plano['Carga Horária (h)'] = pd.to_numeric(df_plano['Carga Horária (h)'], errors='coerce').fillna(0)
        df_plano['Status'] = df_plano['aula_concluida'].apply(lambda x: "✅ Concluído" if x else "🕒 Pendente")

        progresso_geral_display, progresso_trilha_display = calcular_progresso(df_plano)
        
        # --- Métricas Gerais ---
        st.markdown("### Métricas Gerais")
        total_aulas = len(df_plano)
        aulas_concluidas = int(df_plano['aula_concluida'].sum())
        aulas_pendentes = total_aulas - aulas_concluidas
        horas_restantes = df_plano[~df_plano['aula_concluida']]['Carga Horária (h)'].sum()
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Aulas Concluídas", f"{aulas_concluidas}", f"de {total_aulas} aulas")
        col2.metric("Aulas Pendentes", f"{aulas_pendentes}")
        col3.metric("Horas Restantes", f"{horas_restantes:.1f}h")
        st.markdown("##### Progresso Total do Plano")
        st.progress(progresso_geral_display / 100, text=f"{progresso_geral_display:.1f}% Concluído")
        st.divider()

        # --- Progresso por Trilha ---
        st.markdown("### Progresso por Trilha")
        for _, row in progresso_trilha_display.iterrows():
            st.markdown(f"**{row['Trilha']}**")
            st.progress(row['progresso_%'] / 100, text=f"{row['progresso_%']}% concluído ({int(row['aulas_concluidas'])} de {int(row['total_aulas'])} aulas)")
        st.divider()

        # --- Tabela Detalhada Interativa ---
        st.markdown("### Detalhes do Plano de Estudos")
        st.toggle("Mostrar aulas concluídas", key="mostrar_concluidos")

        df_para_exibir = df_plano.copy()
        if not st.session_state.mostrar_concluidos:
            df_para_exibir = df_para_exibir[df_para_exibir['aula_concluida'] == False]
        
        st.session_state.plano_original = df_plano.set_index('id')
        df_editado = st.data_editor(
            df_para_exibir.set_index('id'),
            #...(config da tabela)...
            column_config={
                "Status": "Status", "aula_concluida": st.column_config.CheckboxColumn("Concluído?", default=False),
                "Trilha": "Trilha", "Módulo": "Módulo", "Objetivo": "Objetivo",
                "Carga Horária (h)": st.column_config.NumberColumn("Horas", format="%.1f h"),
                "Dias Necessários": "Dias",
            },
            column_order=["aula_concluida", "Status", "Trilha", "Módulo", "Objetivo", "Carga Horária (h)", "Dias Necessários"],
            use_container_width=True, key="editor_plano"
        )
        
        df_original_exibido = st.session_state.plano_original.loc[df_editado.index]
        mudancas = (df_original_exibido['aula_concluida'] != df_editado['aula_concluida'])
        
        if mudancas.any():
            # --- Lógica de detecção do evento de conclusão ---
            
            # 1. Calcula o progresso ANTES da mudança
            progresso_geral_antes, progresso_trilha_antes = calcular_progresso(st.session_state.plano_original.reset_index())

            # 2. Aplica as mudanças para calcular o progresso DEPOIS
            df_depois = st.session_state.plano_original.reset_index()
            for item_id, mudou in mudancas.items():
                if mudou:
                    novo_status = df_editado.loc[item_id, 'aula_concluida']
                    df_depois.loc[df_depois['id'] == item_id, 'aula_concluida'] = novo_status
            
            progresso_geral_depois, progresso_trilha_depois = calcular_progresso(df_depois)

            # 3. Compara os progressos e define as flags de celebração
            if progresso_geral_antes < 100 and progresso_geral_depois >= 100:
                st.session_state.celebrate_plano_completo = True
            
            merged_progress = pd.merge(progresso_trilha_antes, progresso_trilha_depois, on='Trilha', suffixes=('_antes', '_depois'))
            for _, row in merged_progress.iterrows():
                if row['progresso_%_antes'] < 100 and row['progresso_%_depois'] >= 100:
                    st.session_state.celebrate_trilha_nome = row['Trilha']
                    break # Celebra uma trilha por vez para não poluir a tela

            # 4. Salva as mudanças no banco de dados
            ids_alterados = mudancas[mudancas].index
            for item_id in ids_alterados:
                novo_status = df_editado.loc[item_id, 'aula_concluida']
                repo.update_aula_status(int(item_id), bool(novo_status), user_id)
            
            st.toast("Progresso salvo!")
            st.rerun()