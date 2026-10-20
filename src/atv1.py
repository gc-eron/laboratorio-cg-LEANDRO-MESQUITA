import numpy as np
import streamlit as st

st.title("Computação Gráfica")
st.write("Meu nome é LEANDRO MESQUITA.")
n = st.slider("Tamanho", 2, 64, 8)
img = np.random.randint(0, 256, (n, n), dtype=np.uint8)
st.image(img, caption=f"Imagem {n}x{n}", width=300)
st.write(img)
