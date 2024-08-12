from typing import Annotated

from fastapi import FastAPI, HTTPException

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
    pass 

@app.get("/blogs/{blog_entry_id}", status_code=200)
def get_entry_by_id(blog_entry_id: int, q: str|None = None):
    """_summary_

    Args:
        blog_entry_id (int): _description_
        q (Union[str, None], optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    return {"item_id": blog_entry_id, "q": q}

@app.get("/title/{blog_entry_id}", status_code=200)
def get_entry_by_title(item_id: int, q: str|None = None):
    """_summary_

    Args:
        item_id (int): _description_
        q (Union[str, None], optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    return {"item_id": item_id, "q": q}

@app.post("/blogs", status_code=201)
def add_new_blog_entry(blog: dict):
    """_summary_

    Args:
        blog (dict): _description_
    """
    pass