import streamlit as st
from core.api_cliente import buscar_fotos

def exibir_galeria():
    """
    Renderiza a interface da galeria de fotos em formato de grade (grid).
    """
    lista_de_fotos = buscar_fotos()

    if not lista_de_fotos:
        st.warning("Nenhuma foto encontrada na galeria.")
        return

    st.write(f"Exibindo {len(lista_de_fotos)} fotos encontradas no servidor.")

    COLUNAS_POR_LINHA = 3
    
    colunas = st.columns(COLUNAS_POR_LINHA)

    for indice, foto in enumerate(lista_de_fotos):
        coluna_atual = colunas[indice % COLUNAS_POR_LINHA]
        
        with coluna_atual:
            st.subheader(foto["titulo"])
            
            st.image(
                foto["url"], 
                use_container_width=True, 
                caption=f"Enviada em: {foto['data_upload']}"
            )
            
            st.button("Ver Detalhes", key=f"btn_{foto['id']}")
            
            st.write("")