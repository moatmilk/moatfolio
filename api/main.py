from typing import Annotated, Union

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

import datetime
from pymongo import MongoClient

class MongoDB:
    def __init__(self, host: str="localhost", port: int=27017, db_name: str="blogs") -> None:
        self.client = MongoClient(
            host=host, # localhost is the default in MongoClient
            port=port, # 27017 is the default in MongoClient
            #connect=BlogEntry().model_dump(),
        )
        self.db = self.client[db_name]

    def get_collection(self, name: str):
        """_summary_
        """
        return self.db[name]

    def get_blog_entry_by_object_id(self, entry_id: str):
        """_summary_
        """
        collection = self.get_collection("entries")
        return collection.find_one({"_object": entry_id})

    def get_blog_entry_by_title(self, title: str):
        """_summary_

        Args:
            title (str): _description_
        """
        collection = self.get_collection("entries")
        return collection.find_one({"title": title})                                                                                                                            
    
    def get_all_blogs(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        collection = self.get_collection("entries")
        return collection.find()
    
    def add_blog_entry(self, blog: dict):
        """Add a single blog entry to the collection. Must first verify schema

        Args:
            blog (dict): _description_
        """
        collection = self.get_collection("entries")
        collection.insert_one(blog)

mongo = MongoDB()

app = FastAPI(
    title="Add/retrieve blog entries from Mohammad's personal website",
    summary="Mohammad's Personal Portfolio",
    description="This API will contain the endpoints required to query the backends",
    version="0.5.0",
    redirect_slashes=True,
    contact={
        "name": "Mohammad Rammah",
        # "url": "Mohammad Rammah",
        "email": "mrammah0@gmail.com",
    },
)


@app.get("/")
def read_root():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {
        "automatic interactive api documentation": app.docs_url,
        "alternative interactive api documentation": app.redoc_url,
    }

@app.get("/health", status_code=200)
def health_checker():
    """_summary_
    """
    return JSONResponse(content={"message": "API is running!"}, status_code=200)


@app.get("/blogs/{blog_entry_id}", status_code=200)
def get_entry_by_id(blog_entry_id: int, q: Union[str,None] = None):
    """_summary_

    Args:
        blog_entry_id (int): _description_
        q (Union[str, None], optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    return mongo.get_blog_entry_by_object_id(blog_entry_id)

@app.get("/blogs/", status_code=200)
def get_entry_by_title(title: str="hello"):
    """_summary_

    Args:
        item_id (int): _description_
        q (Union[str, None], optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    return mongo.get_blog_entry_by_title(title)

@app.get("/blogs", status_code=200)
def get_all_blog_entries():
    """_summary_

    Args:
        item_id (int): _description_
        q (Union[str, None], optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    return mongo.get_all_blogs()

@app.post("/blogs", status_code=201)
def add_new_blog_entry(blog: dict):
    """_summary_

    Args:
        blog (dict): _description_
    """
    return mongo.add_blog_entry(blog)
