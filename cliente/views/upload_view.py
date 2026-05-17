import streamlit as st
from core.api_cliente import fazer_upload_foto

def exibir_upload():
    """
    Renderiza a interface para seleção de arquivos e envio de fotos.
    """
    st.write("Selecione uma foto do seu computador para simular o envio para o servidor.")

    titulo = st.text_input(
        label="Título da Imagem", 
        placeholder="Ex: Minha viagem para a praia",
        max_chars=50
    )

    arquivo_enviado = st.file_uploader(
        label="Escolha uma imagem", 
        type=["png", "jpg", "jpeg"]
    )

    if arquivo_enviado is not None:
        st.write("---")
        st.subheader("Visualização da foto selecionada:")
        st.image(arquivo_enviado, width=300)
        
        botao_enviar = st.button(
            label="Enviar Foto para a API", 
            disabled=not titulo.strip()
        )
        
        if not titulo.strip():
            st.caption("Digite um título acima para liberar o botão de envio.")

        if botao_enviar:
            with st.spinner("Enviando arquivo para o servidor..."):
                sucesso, mensagem = fazer_upload_foto(arquivo_enviado, titulo)
                
            if sucesso:
                st.success(mensagem)
                st.balloons() 
            else:
                st.error(f"Erro ao enviar: {mensagem}")