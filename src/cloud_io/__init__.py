import pandas as pd
from database_connect import mongo_operation as mongo
import os,sys
from src.constants import *
from src.exception import CustomException

# Below class is used to interact with mongodb for data retrieving and upload operations
class MongoIO:
    mongo_ins=None

    def __init__(self):
        if MongoIO.mongo_ins is None:
            mongo_db_url="mongodb+srv://Umam:12345@cluster0.9ajxfcx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
            if mongo_db_url is None:
                raise Exception(f"Environment Key: {MONGODB_URL_KEY} is not set.")
            MongoIO.mongo_ins=mongo(client_url=mongo_db_url,
                                    database_name=MONGO_DATABASE_NAME)
        self.mongo_ins=MongoIO.mongo_ins

    # def bulk_insert(self, documents, collection_name: str):
    #     """
    #     Inserts multiple documents into a MongoDB collection.
    #     Accepts either a pandas DataFrame or list of dictionaries.
    #     """
    #     try:
    #         # ✅ Convert DataFrame to list of dicts
    #         if isinstance(documents, pd.DataFrame):
    #             documents = documents.to_dict(orient="records")

    #         # ✅ Validate non-empty
    #         if not documents or not isinstance(documents, list):
    #             raise ValueError("bulk_insert: 'documents' must be a non-empty list or DataFrame.")

    #         collection = self.mongo_ins[collection_name]
    #         result = collection.insert_many(documents)

    #         print(f"✅ Inserted {len(result.inserted_ids)} documents into '{collection_name}' collection.")
    #         return result

    #     except Exception as e:
    #         raise CustomException(e, sys)

    def store_reviews(self,product_name: str,reviews: pd.DataFrame):
        try:
            # if reviews is None or reviews.empty:
            #     raise ValueError("store_reviews: DataFrame is empty. Nothing to insert.")
            collection_name=product_name.replace(" ","_")
            self.mongo_ins.bulk_insert(reviews,collection_name)
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def get_reviews(self,product_name: str):
        try:
            data=self.mongo_ins.find(
                collection_name=product_name.replace(" ","_")
            )
            
            return data
        
        except Exception as e:
            raise CustomException(e,sys)