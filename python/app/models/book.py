from typing import Optional, List

from pydantic import BaseConfig, BaseModel


class Book(BaseModel):
    title: str
    description: Optional[str] = None
    tags: List[str]

    class Config(BaseConfig):
        title = 'Deep Learning'
        description = 'A cook book for deep learning practitioner'
        tags = ['DeepLearning']


class BookFilterParams(BaseModel):
    title: str
    tags: List[str]
    limit: int = 10


class BookInDB(BaseModel):
    pass

