import streamlit as st
from PIL import Image

st.title("🔬 Analisador de Bolhas B-Foam")

# Campos de preenchimento do usuário
st.sidebar.header("Dados da Amostra")
amostra = st.sidebar.text_input("Número da Amostra", "001")
teste = st.sidebar.text_input("Número do Teste", "01")
tipo = st.sidebar.selectbox("Tipo do Teste", ["A", "B", "C"])
versao = st.sidebar.selectbox("Versão", ["V08", "V09", "V10"])

# Upload da imagem
uploaded_file = st.file_uploader("Suba a imagem...", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    # Redimensionando a imagem para ficar menor (ex: 500 pixels de largura)
    width = 500
    w_percent = (width / float(image.size[0]))
    h_size = int((float(image.size[1]) * float(w_percent)))
    image_resized = image.resize((width, h_size))
    
    st.image(image_resized, caption=f'Amostra {amostra} - Teste {teste}')
    
    # Botão para salvar (aqui entra a lógica de salvar no banco)
    if st.button("Salvar Amostra"):
        nome_arquivo = f"{amostra}_{teste}_{tipo}_{versao}"
        st.success(f"Dados prontos para salvar: {nome_arquivo}")
        # Em breve: Conectaremos com Google Sheets aqui!
