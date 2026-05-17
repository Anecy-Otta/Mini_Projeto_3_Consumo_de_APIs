import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from views.gallery_view import exibir_galeria
from views.upload_view import exibir_upload

st.set_page_config(
    page_title="The gallery - Cliente API de Fotos",
    page_icon="📸",
    layout="wide"
)

st.sidebar.title("Navegação")
aba_selecionada = st.sidebar.radio(
    "Ir para:",
    ["Visualizar Galeria", "Fazer Upload de Fotos"]
)

st.title("📸 The gallery")
st.divider()

if aba_selecionada == "Visualizar Galeria":
    st.header("🖼️ Ver fotos")
    exibir_galeria()
    
elif aba_selecionada == "Fazer Upload de Fotos":
    st.header("📤 Enviar Nova Foto")
    exibir_upload()