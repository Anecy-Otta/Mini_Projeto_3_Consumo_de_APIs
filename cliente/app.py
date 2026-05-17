import streamlit as st

st.set_page_config(
    page_title="The gallery",
    page_icon="📸",
    layout="wide"
)

st.sidebar.title("Navegação")
aba_selecionada = st.sidebar.radio(
    "Ir para:",
    ["Visualizar Galeria", "Fazer Upload de Fotos"]
)

st.title("📸 The gallery")
st.write("Bem-vindo ao cliente do nosso servidor de fotos. Use o menu lateral para navegar.")

st.divider()

if aba_selecionada == "Visualizar Galeria":
    st.header("🖼️ Ver Fotos")
    st.info("O esqueleto da galeria foi criado com sucesso. Próximo passo: carregar as fotos.")
    
elif aba_selecionada == "Fazer Upload de Fotos":
    st.header("📤 Enviar Nova Foto")
    st.info("O esqueleto de upload foi criado com sucesso. Próximo passo: adicionar o seletor de arquivos.")
    
