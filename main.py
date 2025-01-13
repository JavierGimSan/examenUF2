from fastapi import FastAPI
from pydantic import BaseModel
from conn import connection_db

app = FastAPI()

#EXERCICI 1, BaseModel
class Formulario(BaseModel):
    nombre: str
    apellido: str
    correo_electronico: str
    descripcion: str | None
    curso: int
    anyo: int
    direccion: str
    codigo_postal: int | None
    password: str

#EXERCICI 2, funció per inserir un usuari a la BD
def create_user(user: Formulario):
    try:
        conn = connection_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (nombre, apellido, correo_electronico, descripcion, curso, anyo, direccion, codigo_postal, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",
            (user.nombre, user.apellido, user.correo_electronico, user.descripcion, user.curso, user.anyo, user.direccion, user.codigo_postal, user.password),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return user
    except Exception as e:
        raise Exception(f"Error al añadir usuario: {e}")

#EXERCICI 2. Mètode post per executar la funció anterior.
@app.post("/afegir_usuari", response_model=dict)
async def add_user(user: Formulario):
    try:
        create_user(user)
        return {"nombre": user.nombre}
    except Exception as e:
        return {"error": str(e)}