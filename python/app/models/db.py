# from bson import ObjectId
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Schema 


class DateTimeModelMixin(BaseModel):
    created_at: Optional[datetime] = Schema(..., alias='createdAt')
    updated_at: Optional[datetime] = Schema(..., alias='updatedAt')


class DBModelMixin(DateTimeModelMixin):
    _id: Optional[str]


