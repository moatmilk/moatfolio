from typing import Annotated, Union

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

import datetime
from pymongo import MongoClient

class MongoDB:
    def __init__(self, host: str="localhost", port: int=27017, db_name: str="blogs") -> None:
        self.client = MongoClient("mongodb://mongodb:27017/")
            #host=host, # localhost is the default in MongoClient
            #port=port, # 27017 is the default in MongoClient
            #connect=BlogEntry().model_du
        self.db = self.client[db_name]

    def get_collection(self, name: str):
        """_summary_
        """
        return self.db[name]

    def get_blog_entry_by_object_id(self, entry_id: str):
        """_summary_
        """
        collection = self.get_collection("entries")
        return self.serialize_document(collection.find_one({"id": str(entry_id)}))

    def get_blog_entry_by_title(self, title: str):
        """_summary_

        Args:
            title (str): _description_
        """
        collection = self.get_collection("entries")
        return self.serialize_document(collection.find_one({"title": title}))                                                                                                                            
    
    def get_all_blogs(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        collection = self.get_collection("entries")
        print(collection)
        docs = collection.find()
        blogs = [self.serialize_document(doc) for doc in docs]
        return blogs
    
    @staticmethod
    def serialize_document(doc):
       """Convert MongoDB document to a serializable format."""
       doc['_id'] = str(doc['_id'])  # Convert ObjectId to string
       return doc

    def add_blog_entry(self, blog: dict):
        """Add a single blog entry to the collection. Must first verify schema

        Args:
            blog (dict): _description_
        """
        print(blog)
        collection = self.get_collection("entries")
        collection.insert_one(blog)

    def update_blog_entry(self, doc):
        collection = self.get_collection("entries")
        update = {"$set": doc}
        collection.update_one({"id": str(doc["id"])}, update)

    def delete_blog_entry_by_id(self, doc_id):
        collection = self.get_collection("entries")
        collection.delete_one({"id": str(doc_id)})

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
def get_entry_by_id(blog_entry_id: str):
    """grab blof entry by id

    Args:
        blog_entry_id (int): _description_

    Returns:
        _type_: _description_
    """
    return mongo.get_blog_entry_by_object_id(blog_entry_id)

@app.get("/blogs", status_code=200)
def get_entry_by_title(title: str="hello"):
    """Get the blog associated with the path parameter you've specified. in this case given the title you have provided 

    Args:
        title (str): the title of the blog you would like to view

    Returns:
        list[dict]: all the blogs in mongodb
    """
    return mongo.get_blog_entry_by_title(title)

@app.get("/blogs/", status_code=200)
def get_all_blog_entries():
    """Return all the blogs from the database

    Returns:
        _type_: _description_
    """
    return mongo.get_all_blogs()

@app.post("/blogs/", status_code=201)
def add_new_blog_entry(blog: dict):
    """given request body, add entry to mongodb

    Args:
        blog (dict): the entry you would like to add
    """
    return mongo.add_blog_entry(blog)

@app.put("/blogs/remove/{blog_id}", status_code=201)
def delete_blog_entry(blog_id: int):
    """given request body, add entry to mongodb

    Args:
        blog (dict): the entry you would like to add
    """
    return mongo.delete_blog_entry_by_id(blog_id)

@app.put("/blogs/update/",  status_code=201)
def update_blog_entry(blog:dict):
    """given request body, add entry to mongodb

    Args:
        blog (dict): the entry you would like to add
    """
    return mongo.update_blog_entry(blog)
