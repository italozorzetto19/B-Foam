import streamlit as st
import base64 
from PIL import Image

# Configuração da Página
st.set_page_config(page_title="B-Foam MSB", page_icon="🔬", layout="centered")

# --- FUNÇÃO PARA CONVERTER IMAGEM PARA BASE64 ---
def get_image_as_base64(path):
    with open(path, "rb") as image_file:
        data = base64.b64encode(image_file.read()).decode()
    return f"data:image/png;base64,{data}"

# --- ESTILIZAÇÃO CSS CUSTOMIZADA ---
st.markdown("""
<style>
    /* Cabeçalho centralizado e com ajuste de texto */
    #header-container {
        background-color: white; color: black; padding: 20px; border-radius: 10px; margin-bottom: 30px;
        display: flex; align-items: center; justify-content: center; /* Centraliza conteúdo */
        width: 100%; text-align: center;
    }
    
    /* Centralizar botão */
    .stButton { display: flex; justify-content: center; }
    .stButton>button { width: 80%; border-radius: 10px; }

    /* Ajuste para evitar quebra de linha estranha */
    .card { 
        background-color: #1E3A5F; padding: 20px; border-radius: 15px; 
        border: 1px solid #2E7BCF; text-align: center; min-height: 250px;
        display: flex; flex-direction: column; justify-content: flex-start;
    }

    .titulo-amarelo { 
        color: #FFD700; 
        font-size: 2.5em;      /* Aumentei para 2.5em (pode ajustar para mais ou menos) */
        font-weight: bold; 
        text-align: center;    /* Centraliza o texto */
        margin-top: 20px;      /* Espaço superior */
        margin-bottom: 20px;   /* Espaço inferior para separar dos cards */
    }

    .card { 
        background-color: #1E3A5F; padding: 20px; border-radius: 15px; 
        border: 1px solid #2E7BCF; text-align: center; min-height: 180px;
    }
    .card h3 { color: #FFFFFF; margin-bottom: 5px; }
    .card p { color: #B9D1EA; font-size: 0.9em; margin: 0; }
    
    .stButton>button { width: 100%; border-radius: 10px; }
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
    
    # Cabeçalho
    try:
        logo_base64 = get_image_as_base64("logo-msb.png") 
        st.markdown(f'''<div id="header-container"><img src="{logo_base64}" alt="MSB Logo">
                      <div><h1>B-Foam</h1><p>Engenharia - MSB - Plataforma de Análise</p></div></div>''', unsafe_allow_html=True)
    except: st.error("Logotipo não encontrado.")

    st.markdown('<p class="titulo-amarelo">Selecione o tipo de análise desejada:</p>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown('<div class="card"><h3>Meia-Vida</h3><p>Análise do tempo de decaimento das microbolhas para determinar a longevidade da espuma.</p></div>', unsafe_allow_html=True)
        if st.button("Selecionar", key="mv"): ir_para_cadastro("Meia-Vida")
    
    with c2:
        # Removido qualquer espaçamento extra antes do título
        st.markdown('<div class="card"><h3>Granulometria</h3><p>Medição do tamanho e distribuição das bolhas para avaliar a homogeneidade da amostra.</p></div>', unsafe_allow_html=True)
        if st.button("Selecionar", key="gr"): ir_para_cadastro("Granulometria")
    
    with c3:
        st.markdown('<div class="card"><h3>Estabilidade</h3><p>Avaliação da resistência estrutural da espuma sob variações de pressão e tempo.</p></div>', unsafe_allow_html=True)
        if st.button("Selecionar", key="ed"): ir_para_cadastro("Estabilidade Dinâmica")

    # Sidebar apenas na tela de seleção
    with st.sidebar:
        st.header("Vídeos de Apoio")
        st.video("https://youtu.be/hY5K55Ha2pg")
        st.write("Assista ao teste de medição do tamanho de bolhas.")

# --- TELA 2: CADASTRO DE TESTE ---
elif st.session_state.pagina == 'cadastro':
    try:
        logo_base64 = get_image_as_base64("logo-msb.png") 
        st.markdown(f'''<div id="header-container"><img src="{logo_base64}" alt="MSB Logo">
                      <div><h1>Analisador B-Foam</h1><p>Medical System do Brasil - Plataforma de Análise</p></div></div>''', unsafe_allow_html=True)
    except: pass
    
    st.markdown("---")
    st.subheader(f"Ficha de Cadastro: {st.session_state.tipo_selecionado}")
    
    if st.button("⬅️ Voltar ao Menu Principal"):
        st.session_state.pagina = 'selecao'
        st.rerun()
    
    tab1, tab2 = st.tabs(["➕ Cadastrar Novo Teste", "🔍 Buscar Histórico"])
    with tab1:
        st.write("Aguardando upload da imagem para análise...")
