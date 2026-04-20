import streamlit as st
from PIL import Image

st.set_page_config(page_title="Visualizador de Bolhas", layout="centered")

st.title("🔬 Visualizador de Amostras")
st.write("Carregue uma imagem abaixo para visualizar.")

# Apenas o carregador e a exibição
uploaded_file = st.file_uploader("Escolha a imagem da espuma...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagem Carregada com Sucesso', use_column_width=True)
    st.success("Imagem exibida!")
