import streamlit as st
from PIL import Image

# Configuração da Página
st.set_page_config(page_title="B-Foam MSB", page_icon="🔬", layout="centered")

# --- ESTILIZAÇÃO CSS (Cards e Layout) ---
st.markdown("""
<style>
    .card { background-color: #f8f9fa; padding: 20px; border-radius: 10px; border: 1px solid #e0e0e0; text-align: center; }
    .stButton>button { width: 100%; border-radius: 8px; }
</style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
col1, col2 = st.columns([1, 3])
with col1:
    try:
        # CERTIFIQUE-SE DE QUE O NOME DO ARQUIVO É EXACTAMENTE ESTE:
        st.image("logo-msb.png", use_column_width=True) 
    except:
        st.error("Logo não encontrada")
with col2:
    st.title("Analisador B-Foam")
    st.caption("Medical System do Brasil - Plataforma de Análise")

st.markdown("---")

# --- NAVEGAÇÃO E MODULARIZAÇÃO ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'selecao'

def ir_para_cadastro(tipo):
    st.session_state.pagina = 'cadastro'
    st.session_state.tipo_selecionado = tipo

# Tela de Seleção
if st.session_state.pagina == 'selecao':
    st.subheader("Selecione o tipo de análise:")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="card"><h3>⏱️</h3><p>Meia-Vida</p></div>', unsafe_allow_html=True)
        if st.button("Selecionar", key="mv"): ir_para_cadastro("Meia-Vida")
    with c2:
        st.markdown('<div class="card"><h3>🫧</h3><p>Granulometria</p></div>', unsafe_allow_html=True)
        if st.button("Selecionar", key="gr"): ir_para_cadastro("Granulometria")
    with c3:
        st.markdown('<div class="card"><h3>📉</h3><p>Estabilidade</p></div>', unsafe_allow_html=True)
        if st.button("Selecionar", key="ed"): ir_para_cadastro("Estabilidade Dinâmica")

# Tela de Cadastro (Modularizada)
elif st.session_state.pagina == 'cadastro':
    st.subheader(f"Análise: {st.session_state.tipo_selecionado}")
    if st.button("⬅️ Voltar"):
        st.session_state.pagina = 'selecao'
        st.rerun()
    
    tab1, tab2 = st.tabs(["➕ Novo Teste", "🔍 Buscar Histórico"])
    
    with tab1:
        # AQUI VOCÊ CHAMARÁ AS FUNÇÕES MODULARIZADAS NO FUTURO
        if st.session_state.tipo_selecionado == "Granulometria":
            st.info("Carregue a imagem para iniciar a análise de Granulometria.")
            # Exemplo de chamada modular:
            # from utils_bolhas import processar
            # processar()
        else:
            st.write(f"Interface para {st.session_state.tipo_selecionado} em desenvolvimento.")
