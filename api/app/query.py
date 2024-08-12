import datetime

from pymongo import MongoClient

from api.app.schema import BlogEntry

class MongoDB:
    def __init__(self, host: str="localhost", port: int=27017, db_name: str="blogs") -> None:
        self.client = MongoClient(
            host=host, # localhost is the default in MongoClient
            port=port, # 27017 is the default in MongoClient
            connect=BlogEntry().model_dump(),
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

    def add_blog_entry(self, blog: dict):
        """Add a single blog entry to the collection. Must first verify schema

        Args:
            blog (dict): _description_
        """
        pass
    
    def get_blogs_between_date_range(self, start: datetime, end: datetime, relation: str):
        """_summary_

        Args:
            start (datetime): _description_
            end (datetime): _description_
            relation (str): _description_

        Returns:
            _type_: _description_
        """
        pass

    def get_all_blogs(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        pass

    @staticmethod
    def verify_schema(blog: dict):
        """_summary_

        Args:
            blog (dict): _description_

        Returns:
            _type_: _description_
        """
        return BlogEntry(**blog).model_dump()