from email.policy import default
from ensurepip import version
from operator import gt, lt
from turtle import title
from typing import List, Optional, Any, Dict

from fastapi.responses import JSONResponse
from fastapi import Path, Query, Response, Header, Depends

from time import sleep
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from models import Curso, cursos

def fake_db():
    try:
        print('Abrindo conexões com banco de dados...')
        sleep(1)
    finally:
        print('Fechando conexão com o banco de dados...')
        sleep(1)


app = FastAPI(title = 'Api de Curso de FastAPI', 
    version = 0.01,
    description = 'Uma API para estudo de FastAPI'
)

@app.get('/cursos', description = 'Retorna todos os cursos ou uma lista vazia.', 
        summary = 'Retorna todos os cursos.',
        response_model = List[Curso], 
        response_description = 'Cursos encontrados com sucesso.')
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos

@app.get('/cursos/{curso_id}')
async def get_cursos(curso_id: int = Path(
    default = None, title='ID do curso', description='Deve ser entre 1 e 2', gt=0, lt=3)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.')

@app.post('/cursos', status_code= status.HTTP_201_CREATED, response_model = Curso)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id

        return curso
    else:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail=f'Não existe curso com o ID {curso_id}')

@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        
        return Response(status_code = status.HTTP_204_NO_CONTENT)
        #return JSONResponse(status_code = status.HTTP_204_NO_CONTENT)
    else:
         raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail=f'Não existe curso com o ID {curso_id}')  

@app.get('/calculadora')
async def calcular(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=10), x_geek: str = Header(default=None), c: Optional[int] = None):
    soma: int = a+b
    if c:
        soma += c
        
    
    print(f'X-GEEK: {x_geek}')
    return {"resultado": soma}

if __name__ == '__main__':
    import uvicorn 

    uvicorn.run("main:app", host="127.0.0.1",
        port=8000, log_level="info", debug=True, reload=True)