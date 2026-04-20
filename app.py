import streamlit as st
from PIL import Image

# Configuração da página para layout centralizado e ícone personalizado
st.set_page_config(page_title="B-Foam MSB", page_icon="🔬", layout="centered")

# --- CABEÇALHO COM LOGO E TÍTULO ---
col_logo, col_titulo = st.columns([1, 4]) # Proporção 1:4

with col_logo:
    # Carrega a imagem da logo (certifique-se de que o arquivo image_19.png está na mesma pasta no GitHub)
    try:
        logo = Image.open("image_19.png")
        st.image(logo, use_column_width=True)
    except FileNotFoundError:
        st.warning("⚠️ Arquivo 'image_19.png' não encontrado. Suba-o para o GitHub.")

with col_titulo:
    st.title("Analisador de Bolhas B-Foam")
    st.write("Medical System do Brasil - Plataforma de Análise de Espuma")

st.markdown("---") # Linha divisória

# --- ESTILIZAÇÃO CSS (Opcional - para deixar mais parecido com o Power BI) ---
# Você pode remover se preferir o padrão puro do Streamlit
st.markdown("""
<style>
    /* Estiliza os botões */
    .stButton>button {
        border-radius: 10px;
        background-color: #f0f2f6; /* Cinza claro no hover */
        border: 1px solid #d3d3d3;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #2e7bcf; /* Azul MSB no hover */
        color: white;
    }
    
    /* Estiliza os campos de input */
    .stTextInput>div>div>input {
        background-color: transparent !important;
        border-bottom: 2px solid #2e7bcf !important;
    }
</style>
""", unsafe_allow_html=True)

# --- SISTEMA DE NAVEGAÇÃO ENTRE TELAS ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'selecao'

def ir_para_cadastro(tipo_teste):
    st.session_state.pagina = 'cadastro'
    st.session_state.tipo_selecionado = tipo_teste

if st.session_state.pagina == 'selecao':
    st.subheader("Selecione o tipo de análise desejada:")
    
    # Grid de botões (3 colunas)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Usando ícones para dar um visual mais moderno
        st.markdown("### ⏱️")
        if st.button("Meia-Vida", key="btn_mv"): ir_para_cadastro("Meia-Vida")
    
    with col2:
        st.markdown("### 🫧")
        if st.button("Granulometria", key="btn_gr"): ir_para_cadastro("Granulometria")
    
    with col3:
        st.markdown("### 📉")
        if st.button("Estabilidade Dinâmica", key="btn_ed"): ir_para_cadastro("Estabilidade Dinâmica")

elif st.session_state.pagina == 'cadastro':
    st.header(f"Ficha de Cadastro: {st.session_state.tipo_selecionado}")
    
    # Botão para voltar com um visual mais amigável
    if st.button("⬅️ Voltar ao Menu Principal"):
        st.session_state.pagina = 'selecao'
        st.rerun()

    # Reutilizando a interface de Tabs (Abas) que você já criou
    aba_novo, aba_busca = st.tabs(["➕ Cadastrar Novo Teste", "🔍 Buscar Histórico"])
    
    with aba_novo:
        # Adicione aqui os seus campos de input específicos
        st.info(f"Interface para novo teste de {st.session_state.tipo_selecionado} aberta.")
        amostra = st.text_input("Número da Amostra (Ex: 001-A)")
