import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
altura, largura = img.shape[0], img.shape[1]

st.header("8. Negativo")
col1, col2 = st.columns(2)
negativo = 255 - img
col1.image(img, caption="original")
col2.image(negativo, caption="negativo")

st.header("9. Recorte")
col1, col2 = st.columns(2)
linha = col1.slider("Linha inicial", 0, altura - 1, altura // 3)
coluna = col1.slider("Coluna inicial", 0, largura - 1, largura // 5)
lado = col1.slider("Lado do quadrado", 10, largura, largura // 2)
recorte = img[linha:linha + lado, coluna:coluna + lado]
col2.image(recorte, caption="recorte")

st.header("11. Espelhamento")
col1, col2 = st.columns(2)
col1.image(img[:, ::-1], caption="horizontal")
col2.image(img[::-1, :], caption="vertical")

st.header("12. Simetria")
col1, col2 = st.columns(2)
meio = largura // 2
esquerda = img[:, 0:meio]
simetrica = img.copy()
simetrica[:, largura - meio:largura] = esquerda[:, ::-1]
col1.image(img, caption="original")
col2.image(simetrica, caption="simétrica")

st.header("20. Pixel art")
col1, col2 = st.columns(2)
passo = col1.slider("Passo", 2, 60, 16)
pequena = img[::passo, ::passo]
grande = pequena.repeat(passo, axis=0).repeat(passo, axis=1)
col2.image(grande, caption="pixel art")
