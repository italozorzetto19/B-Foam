import streamlit as st

st.title("🔬 Analisador de Bolhas B-Foam")

# Variável de sessão para controlar a tela
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'selecao'

def ir_para_cadastro(tipo_teste):
    st.session_state.pagina = 'cadastro'
    st.session_state.tipo_selecionado = tipo_teste

if st.session_state.pagina == 'selecao':
    st.subheader("Selecione o tipo de análise:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Meia-Vida"): ir_para_cadastro("Meia-Vida")
    with col2:
        if st.button("Granulometria"): ir_para_cadastro("Granulometria")
    with col3:
        if st.button("Estabilidade Dinâmica"): ir_para_cadastro("Estabilidade Dinâmica")

elif st.session_state.pagina == 'cadastro':
    st.subheader(f"Cadastro: {st.session_state.tipo_selecionado}")
    
    # Botão para voltar
    if st.button("⬅️ Voltar ao Menu"):
        st.session_state.pagina = 'selecao'
        st.rerun()

    # Aqui você insere a lógica que já tínhamos feito (Tabs, Upload, etc)
    aba_novo, aba_busca = st.tabs(["➕ Novo Teste", "🔍 Buscar Teste"])
    with aba_novo:
        # Seus campos de input aqui...
        st.write("Interface de cadastro aberta!")
