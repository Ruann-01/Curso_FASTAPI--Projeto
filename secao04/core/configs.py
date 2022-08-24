from string import octdigits
from turtle import st
from typing import List

from pydantic import BaseSettings, AnyHttpUrl

from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    """Configurações gerais usadas na aplicação"""
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://cyber:curso123@localhost:5432/faculdade"
    DBBaseModel: declarative_base()

class Config:
    case_sensitive = True

settings = Settings()