import numpy as np
import streamlit as st


def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Imagem como matriz")

amarelo = (255, 255, 0)
vermelho = (255, 0, 0)

bandeira = np.zeros((16, 24, 3), dtype=np.uint8)

bandeira[:] = vermelho
bandeira[2, 4] = amarelo
bandeira[3, 2:7] = amarelo
bandeira[4, 3:6] = amarelo
bandeira[5, 3] = amarelo
bandeira[5, 5] = amarelo

bandeira[1, 8] = amarelo
bandeira[3, 10] = amarelo
bandeira[6, 10] = amarelo
bandeira[8, 8] = amarelo

st.image(ampliar(bandeira))
