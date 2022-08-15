from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from models import Curso

app = FastAPI()

cursos = {
    1:{
        "titulo": "Programação",
        "aulas": 110,
        "horas":58
    },
    2:{
        "titulo": "Data Science",
        "aulas": 112,
        "horas":54
    }
}

@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_cursos(curso_id: int):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.')

@app.post('/cursos')
async def post_curso(curso: Curso):
    if curso.id not in cursos:
        cursos[curso.id] = curso
        return curso
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=f"Já existe um curso com o ID {curso.id}")

if __name__ == '__main__':
    import uvicorn 

    uvicorn.run("main:app", host="127.0.0.1",
        port=8000, log_level="info", debug=True, reload=True)