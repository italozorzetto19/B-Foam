import streamlit as st
from PIL import Image

# Configuração da Página (Título e Ícone)
st.set_page_config(page_title="B-Foam MSB", page_icon="🔬", layout="centered")

# --- CABEÇALHO ---
col1, col2 = st.columns([1, 3])
with col1:
    try:
        # Busca o nome correto que você mencionou:
        st.image("novo-msb.png", use_column_width=True) 
    except:
        st.error("Logo 'novo-msb.png' não encontrada.")
with col2:
    st.title("Analisador B-Foam")
    st.caption("Medical System do Brasil - Plataforma de Análise")

st.markdown("---")

# --- ESTILIZAÇÃO CSS CUSTOMIZADA (Para combinar com o fundo escuro) ---
st.markdown("""
<style>
    /* Estiliza os Cards para ficarem com fundo azul-marinho */
    .card { 
        background-color: #172A46; /* Mesma cor do secondaryBackgroundColor */
        padding: 25px; 
        border-radius: 12px; 
        border: 1px solid #2E7BCF; # Borda azul MSB
        text-align: center;
        margin-bottom: 15px;
        transition: 0.3s;
    }
    .card:hover { border-width: 2px; } /* Efeito de destaque no hover */
    
    /* Estiliza os botões para ficarem com cantos arredondados e cor azul */
    .stButton>button { 
        width: 100%; 
        border-radius: 10px; 
        background-color: transparent; 
        border: 2px solid #2E7BCF; # Borda azul MSB
        color: white; 
    }
    .stButton>button:hover {
        background-color: #2E7BCF; /* Preenche com azul no hover */
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# --- NAVEGAÇÃO ENTRE TELAS (State Management) ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'selecao'

def ir_para_cadastro(tipo):
    st.session_state.pagina = 'cadastro'
    st.session_state.tipo_selecionado = tipo

# --- TELA 1: SELEÇÃO DE ANÁLISE ---
if st.session_state.pagina == 'selecao':
    st.subheader("Selecione o tipo de análise desejada:")
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

# --- TELA 2: CADASTRO DE TESTE (MODULARIZADA) ---
elif st.session_state.pagina == 'cadastro':
    st.subheader(f"Ficha de Cadastro: {st.session_state.tipo_selecionado}")
    
    # Botão para voltar com estilo
    if st.button("⬅️ Voltar ao Menu Principal"):
        st.session_state.pagina = 'selecao'
        st.rerun()
    
    tab1, tab2 = st.tabs(["➕ Cadastrar Novo Teste", "🔍 Buscar Histórico"])
    
    with tab1:
        # Espaço reservado para carregar as funções externas (Modularização)
        st.write("Aguardando upload da imagem para análise...")
