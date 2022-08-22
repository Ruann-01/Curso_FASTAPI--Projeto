from multiprocessing.sharedctypes import Value
from typing import Optional

from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validar_titulo(cls, value: str):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O titulo deve ter pelo menos três palavras.')

        return value

cursos = [
    Curso(id=1,titulo= "Programação", aulas= 110, horas= 58),
    Curso(id=2,titulo= "Data Science", aulas= 112, horas= 54),
]