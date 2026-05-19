from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
import shutil
import uuid
from pathlib import Path
from datetime import datetime

app = FastAPI(title="The Gallery")

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

ALLOWED_TYPES = {"image/jpeg", "image/png", "image/gif", "image/webp"}


def get_photos():
    photos = []
    for f in sorted(UPLOAD_DIR.iterdir(), key=lambda x: x.stat().st_mtime, reverse=True):
        if f.is_file():
            stat = f.stat()
            photos.append({
                "id": f.stem,
                "filename": f.name,
                "url": f"/uploads/{f.name}",
                "size": stat.st_size,
                "uploaded_at": datetime.fromtimestamp(stat.st_mtime).strftime("%d/%m/%Y %H:%M"),
            })
    return photos


@app.get("/fotos")
def listar_fotos():
    return {"fotos": get_photos(), "total": len(get_photos())}


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail=f"{file.filename}: tipo não permitido")
    ext = Path(file.filename).suffix.lower()
    nome = f"{uuid.uuid4().hex}{ext}"
    dest = UPLOAD_DIR / nome
    with open(dest, "wb") as out:
        shutil.copyfileobj(file.file, out)
    return {"filename": nome, "url": f"/uploads/{nome}"}


@app.delete("/fotos/{photo_id}")
def deletar_foto(photo_id: str):
    for f in UPLOAD_DIR.iterdir():
        if f.stem == photo_id:
            f.unlink()
            return {"deletada": True, "id": photo_id}
    raise HTTPException(status_code=404, detail="Foto não encontrada")

from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
async def index():
    with open("static/index.html") as f:
        return f.read()


app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")