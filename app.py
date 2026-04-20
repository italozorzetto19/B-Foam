import streamlit as st
import base64 # Importação necessária para ler a imagem e colocar no HTML
from PIL import Image

# Configuração da Página
st.set_page_config(page_title="B-Foam MSB", page_icon="🔬", layout="centered")

# --- FUNÇÃO PARA CONVERTER IMAGEM PARA BASE64 ---
# Necessária para renderizar a imagem dentro do cabeçalho HTML customizado
def get_image_as_base64(path):
    with open(path, "rb") as image_file:
        data = base64.b64encode(image_file.read()).decode()
    return f"data:image/png;base64,{data}"

# --- ESTILIZAÇÃO CSS CUSTOMIZADA (Cabeçalho Branco e Cards) ---
st.markdown("""
<style>
    /* 1. ESTILO DO CABEÇALHO BRANCO UNIFICADO */
    #header-container {
        background-color: white;
        color: black; /* Texto preto para contrastar com o fundo branco */
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 30px;
        display: flex;
        align-items: center;
        width: 100%;
    }
    #header-container img {
        height: 80px; /* Altura do logotipo */
        margin-right: 25px;
    }
    #header-container h1 {
        margin: 0;
        font-size: 2.2em;
        font-weight: bold;
    }
    #header-container p {
        margin: 0;
        font-size: 1.1em;
        opacity: 0.8;
    }

    /* 2. ESTILO DOS CARDS DE SELEÇÃO */
    .card {
        background-color: #172A46; /* Fundo azul-marinho dos cards */
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #2E7BCF; # Borda azul MSB
        text-align: center;
        margin-bottom: 15px;
        transition: 0.3s;
    }
    .card:hover { border-width: 2px; } /* Efeito de destaque no hover */
    .card img {
        width: 100%; /* Imagem ocupa a largura do card */
        height: 150px; /* Altura fixa para manter os cards alinhados */
        object-fit: contain; /* Ajusta a imagem sem distorcer */
        border-radius: 8px;
        margin-bottom: 15px;
    }

    /* 3. ESTILO DOS BOTÕES DE SELEÇÃO */
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

# --- SISTEMA DE NAVEGAÇÃO E STATE ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'selecao'

def ir_para_cadastro(tipo):
    st.session_state.pagina = 'cadastro'
    st.session_state.tipo_selecionado = tipo

# --- TELA 1: SELEÇÃO DE ANÁLISE ---
if st.session_state.pagina == 'selecao':
    
    # --- RENDERIZAÇÃO DO CABEÇALHO BRANCO CUSTOMIZADO ---
    try:
        # Converter a logo para base64 para o HTML
        logo_base64 = get_image_as_base64("logo-msb.png") 
        
        # Inserir o HTML customizado
        header_html = f'''
        <div id="header-container">
            <img src="{logo_base64}" alt="MSB Logo">
            <div>
                <h1>Analisador B-Foam</h1>
                <p>Medical System do Brasil - Plataforma de Análise</p>
            </div>
        </div>
        '''
        st.markdown(header_html, unsafe_allow_html=True)
        
    except FileNotFoundError:
        st.error("Logotipo 'logo-msb.png' não encontrado no repositório.")
    except Exception as e:
        st.error(f"Erro ao carregar o cabeçalho: {e}")

    # Separador (pode ser o markdown atual)
    st.markdown("---")

    st.subheader("Selecione o tipo de análise desejada:")
    
    # Colunas para os cards
    c1, c2, c3 = st.columns(3)
    
    with c1:
        # Card de Meia-Vida com imagem
        st.markdown('<div class="card">', unsafe_allow_html=True)
        # Placeholder da imagem (depois você troca pelo arquivo real)
        try:
            # Use temporariamente a própria logo como placeholder, como sugerido
            st.image("logo-msb.png", use_column_width=True) 
        except: pass
        st.markdown('<p>Análise de Meia-Vida</p></div>', unsafe_allow_html=True)
        
        if st.button("Selecionar", key="mv"): ir_para_cadastro("Meia-Vida")
    
   # URL formatada para exportação direta do Google Drive (o mesmo ID que você me deu)
    link_video_granulometria = "https://drive.google.com/file/d/13aP2W2rSOOqiqhY2HrlEcUQrhLNE6FKU/view?usp=sharing"

   with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # Agora o player do YouTube funcionará perfeitamente sem bloqueios
    st.video("https://youtu.be/hY5K55Ha2pg")
    
    st.markdown('<p class="titulo-teste-claro">Análise de Granulometria (Estudo de Bolhas)</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("Selecionar", key="gr"): ir_para_cadastro("Granulometria")
    
    with c3:
        # Card de Estabilidade com imagem
        st.markdown('<div class="card">', unsafe_allow_html=True)
        try:
            st.image("logo-msb.png", use_column_width=True) # Placeholder
        except: pass
        st.markdown('<p>Análise de Estabilidade</p></div>', unsafe_allow_html=True)
        
        if st.button("Selecionar", key="ed"): ir_para_cadastro("Estabilidade Dinâmica")

# --- TELA 2: CADASTRO DE TESTE (MODULARIZADA) ---
elif st.session_state.pagina == 'cadastro':
    
    # Renderizar o cabeçalho branco também na tela de cadastro para consistência
    try:
        logo_base64 = get_image_as_base64("logo-msb.png") 
        header_html = f'''
        <div id="header-container">
            <img src="{logo_base64}" alt="MSB Logo">
            <div>
                <h1>Analisador B-Foam</h1>
                <p>Medical System do Brasil - Plataforma de Análise</p>
            </div>
        </div>
        '''
        st.markdown(header_html, unsafe_allow_html=True)
    except: pass
    st.markdown("---")
    
    st.subheader(f"Ficha de Cadastro: {st.session_state.tipo_selecionado}")
    
    # Botão para voltar com estilo
    if st.button("⬅️ Voltar ao Menu Principal"):
        st.session_state.pagina = 'selecao'
        st.rerun()
    
    tab1, tab2 = st.tabs(["➕ Cadastrar Novo Teste", "🔍 Buscar Histórico"])
    
    with tab1:
        # Espaço reservado para as funções de análise específicas
        st.write("Aguardando upload da imagem para análise...")
