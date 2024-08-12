import datetime
from typing import Annotated

from pydantic import BaseModel, Field

class BlogEntry(BaseModel):
    title: str = Field(
        default= None,
        description="",

    )
    body: str = Field(
        default= None,
        description="",

    )
    tags: list[str] = Field(
        default= None,
        description="",

    )
    category: list[str] = Field(
        default= None,
        description="",

    )
    creation_date: datetime = Field(
        default= None,
        description="",

    )
    comments: list[dict] = Field(
        default= None,
        description="",

    )

class User(BaseModel):
    IP: str = Field(
        default= None,
        description="",

    )
    agent: str = Field(
        default= None,
        description="",

    )
    country: str = Field(
        default= None,
        description="",

    )
    coordinates: str = Field(
        default= None,
        description="",

    )
    start_time: datetime = Field(
        default= None,
        description="",

    )
    end_time: datetime = Field(
        default= None,
        description="",

    )
    