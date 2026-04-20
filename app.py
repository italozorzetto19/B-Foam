import streamlit as st
import base64 

# Configuração da Página
st.set_page_config(page_title="B-Foam MSB", page_icon="🔬", layout="centered")

# --- FUNÇÃO PARA CONVERTER IMAGEM PARA BASE64 ---
def get_image_as_base64(path):
    try:
        with open(path, "rb") as image_file:
            data = base64.b64encode(image_file.read()).decode()
        return f"data:image/png;base64,{data}"
    except:
        return ""

# --- ESTILIZAÇÃO CSS CUSTOMIZADA ---
st.markdown("""
<style>
    /* Cabeçalho */
    #header-container {
        background-color: white; color: black; padding: 20px; border-radius: 10px; margin-bottom: 30px;
        display: flex; align-items: center; justify-content: center; width: 100%; text-align: left;
    }
    #header-container img { height: 70px; margin-right: 20px; }
    #header-container h1 { margin: 0; font-size: 1.8em; font-weight: bold; }
    #header-container p { margin: 0; font-size: 0.9em; opacity: 0.8; }

    /* Título Amarelo */
    .titulo-amarelo { color: #FFD700; font-size: 2.2em; font-weight: bold; text-align: center; margin: 30px 0; }

    /* Cards */
    .card { 
        background-color: #1E3A5F; padding: 15px; border-radius: 15px; 
        border: 1px solid #2E7BCF; text-align: center; height: 220px;
        display: flex; flex-direction: column; justify-content: flex-start;
    }
    .card h3 { color: #FFFFFF; margin-top: 0; margin-bottom: 10px; }
    .card p { color: #B9D1EA; font-size: 0.85em; margin: 0; line-height: 1.4; }

    /* Botão Centralizado */
    div.stButton { text-align: center; margin-top: 10px; }
    div.stButton > button { width: 100%; border-radius: 10px; border: 1px solid #2E7BCF; }
</style>
""", unsafe_allow_html=True)

# --- SISTEMA DE NAVEGAÇÃO ---
if 'pagina' not in st.session_state: st.session_state.pagina = 'selecao'

def ir_para_cadastro(tipo):
    st.session_state.pagina = 'cadastro'
    st.session_state.tipo_selecionado = tipo

# --- TELA 1: SELEÇÃO ---
if st.session_state.pagina == 'selecao':
    logo = get_image_as_base64("logo-msb.png") 
    st.markdown(f'''<div id="header-container"><img src="{logo}">
                  <div><h1>B-Foam</h1><p>Engenharia MSB - Plataforma de Análise</p></div></div>''', unsafe_allow_html=True)

    st.markdown('<p class="titulo-amarelo">Selecione o tipo de análise desejada:</p>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown('<div class="card"><h3>Meia-Vida</h3><p>Análise do tempo de decaimento das microbolhas para determinar a longevidade da espuma.</p></div>', unsafe_allow_html=True)
        if st.button("Selecionar", key="mv"): ir_para_cadastro("Meia-Vida")
    
    with c2:
        st.markdown('<div class="card"><h3>Granulometria</h3><p>Medição do tamanho e distribuição das bolhas para avaliar a homogeneidade da amostra.</p></div>', unsafe_allow_html=True)
        if st.button("Selecionar", key="gr"): ir_para_cadastro("Granulometria")
    
    with c3:
        st.markdown('<div class="card"><h3>Estabilidade</h3><p>Avaliação da resistência estrutural da espuma sob variações de pressão e tempo.</p></div>', unsafe_allow_html=True)
        if st.button("Selecionar", key="ed"): ir_para_cadastro("Estabilidade Dinâmica")

    with st.sidebar:
        st.header("Vídeos de Apoio")
        st.video("https://youtu.be/hY5K55Ha2pg")
        st.write("Assista ao teste de medição do tamanho de bolhas.")

# --- TELA 2: CADASTRO ---
elif st.session_state.pagina == 'cadastro':
    st.subheader(f"Ficha de Cadastro: {st.session_state.tipo_selecionado}")
    if st.button("⬅️ Voltar ao Menu Principal"):
        st.session_state.pagina = 'selecao'
        st.rerun()
    
    tab1, tab2 = st.tabs(["➕ Cadastrar Novo Teste", "🔍 Buscar Histórico"])
    with tab1:
        st.write("Aguardando upload da imagem para análise...")
