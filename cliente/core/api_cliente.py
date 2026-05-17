import time

API_BASE_URL = "http://localhost:8000"

def buscar_fotos():
    """
    Simula uma requisição GET para a API para listar as fotos disponíveis.
    Retorna uma lista de dicionários contendo os metadados das imagens.
    """
    fotos_mock = [
        {
            "id": 1,
            "titulo": "Espaço Sideral",
            "url": "https://images.unsplash.com/photo-1506318137071-a8e063b4bec0?w=500",
            "data_upload": "17/05/2026"
        },
        {
            "id": 2,
            "titulo": "Código Python",
            "url": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=500",
            "data_upload": "17/05/2026"
        },
        {
            "id": 3,
            "titulo": "Pomeranian Fofo",
            "url": "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=500",
            "data_upload": "16/05/2026"
        },
        {
            "id": 4,
            "titulo": "Cenário de Montanha",
            "url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=500",
            "data_upload": "15/05/2026"
        }
    ]
    
    return fotos_mock


def fazer_upload_foto(arquivo_binario, titulo_foto):
    """
    Simula uma requisição POST (multipart/form-data) para enviar uma imagem à API.
    Recebe o arquivo vindo do seletor do Streamlit e o título digitado.
    """
    if arquivo_binario is None:
        return False, "Nenhum arquivo enviado."
        
    time.sleep(0.8)
    
    print(f"[MOCK] Enviando arquivo '{arquivo_binario.name}' com o título '{titulo_foto}' para a API...")
    
    return True, f"Sucesso! A foto '{titulo_foto}' foi armazenada (Simulado)."