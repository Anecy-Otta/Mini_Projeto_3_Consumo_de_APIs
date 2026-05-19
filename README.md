# 📸 The Gallery — Mini Projeto 3

## 💡 Motivação

Durante uma viagem em família, cada integrante registrou momentos únicos pelo seu próprio celular.
Na hora de compartilhar, veio a confusão: arquivos enviados por WhatsApp perdendo qualidade,
e-mails com limite de tamanho, links que expiravam...

**The Gallery** nasceu para resolver isso.

Uma plataforma central onde todos os integrantes fazem o upload das suas fotos,
e cada um baixa apenas as que quiser — sem confusão, sem perda de qualidade,
sem limite de mensagens.

> "Uma viagem, muitos fotógrafos, uma galeria só."

---

## 👥 Integrantes

- **Felipe Santuzzi** — Servidor (API)
- **Anecy Otta** — Cliente (Streamlit)

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório
git clone https://github.com/Anecy-Otta/Mini_Projeto_3_Consumo_de_APIs.git
cd Mini_Projeto_3_Consumo_de_APIs

### 2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate

### 3. Instale as dependências
pip install -r requirements.txt

---

## 🖥️ Servidor (FastAPI)

cd server/app
uvicorn main:app --reload

Acesse em: http://localhost:8000
Documentação automática: http://localhost:8000/docs

### Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | / | Interface web da galeria |
| GET | /fotos | Lista todas as fotos |
| POST | /upload | Envia uma nova foto |
| DELETE | /fotos/{id} | Remove uma foto |

---

## 📱 Cliente (Streamlit)

cd cliente
streamlit run app.py

Acesse em: http://localhost:8501

### Funcionalidades

- Visualizar galeria de fotos em grade
- Fazer upload de novas fotos
- Integração com a API do servidor

---

## 🛠️ Tecnologias

- Python 3.13
- FastAPI — servidor da API
- Uvicorn — servidor ASGI
- Streamlit — interface do cliente
- Requests — chamadas HTTP
