import streamlit as st
from core.api_cliente import buscar_fotos, fazer_upload_foto

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
st.write("Bem-vindo ao cliente do nosso servidor de fotos.")
st.divider()

if aba_selecionada == "Visualizar Galeria":
    st.header("🖼️ Ver fotos")
    
    dados_fotos = buscar_fotos()
    print("[DEBUG TERMINAL] Fotos recebidas do mock:", dados_fotos)
    
    st.info("Função mock de listagem conectada! Olhe o terminal do VSCode/Prompt para ver os dados simulados chegando.")
    
elif aba_selecionada == "Fazer Upload de Fotos":
    st.header("📤 Enviar Nova Foto")
    
    sucesso, mensagem = fazer_upload_foto(None, "Foto Teste")
    
    st.info("Função mock de upload conectada com sucesso!")