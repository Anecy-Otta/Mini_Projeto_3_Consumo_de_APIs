import requests

API_BASE_URL = "http://localhost:8000"

def buscar_fotos():
    try:
        response = requests.get(f"{API_BASE_URL}/fotos")
        data = response.json()
        fotos = []
        for foto in data["fotos"]:
            fotos.append({
                "id": foto["id"],
                "titulo": foto["filename"],
                "url": f"{API_BASE_URL}{foto['url']}",
                "data_upload": foto["uploaded_at"]
            })
        return fotos
    except Exception as e:
        return []

def fazer_upload_foto(arquivo_binario, titulo_foto):
    try:
        files = {"file": (arquivo_binario.name, arquivo_binario, "image/jpeg")}
        response = requests.post(f"{API_BASE_URL}/upload", files=files)
        if response.status_code == 200:
            return True, f"Foto '{titulo_foto}' enviada com sucesso!"
        else:
            return False, "Erro ao enviar foto."
    except Exception as e:
        return False, f"Erro de conexão com o servidor: {str(e)}"