import pymongo.errors
from pymongo import MongoClient

import model
import errors.database as db_err

HOST = 'localhost'
PORT = 27017
DATABASE_NAME = 'cc_hw_1'

def mongo_call_dec(func):
    def decorator(*args, **kwargs):
        try:
            # init client and add to functions kwargs. TODO: might move client init to global scope
            client = MongoClient(host=HOST, port=PORT)
            database = client[DATABASE_NAME]
            kwargs.update({'database':database})
            result = func(*args, **kwargs)

        except pymongo.errors.ConnectionFailure:
            raise Exception(f'Could not connect to MongoDB {DATABASE_NAME} at {HOST}:{PORT}')
        except Exception as e:
            raise e
        return result
    return decorator

def _user_from_mongo(mongo_user_dict):
    mongo_user_dict.update({'user_id': mongo_user_dict['_id']})
    mongo_user_dict.pop('_id', None)
    return model.User(**mongo_user_dict)

@mongo_call_dec
def auth_user(username:str, password_hash:str, database:None):
    if 'person' not in database.list_collection_names():
        raise db_err.ItemDoesNotExistError(location=f'{DATABASE_NAME}@{HOST}:{PORT}', name='person')

    person_collection = database['person']
    query = {'username': username, 'password_hash': password_hash}

    if person_collection and person_collection.count_documents(query) == 0:
        raise db_err.ItemDoesNotExistError(location=f'mongodb: Person at {DATABASE_NAME}@{HOST}:{PORT}', name=username)

    result = person_collection.find(query)

    
    return _user_from_mongo(person_as_dict)

@mongo_call_dec
def get_user_by_id(user_id:str, database=None) -> model.User:
    if 'person' not in database.list_collection_names():
        raise db_err.ItemDoesNotExistError(location=f'mongodb: Person at {DATABASE_NAME}@{HOST}:{PORT}', name=user_id)

    person_collection = database['person']
    person_as_dict = person_collection.find({'_id':user_id})[0]
    
    return _user_from_mongo(person_as_dict)

@mongo_call_dec
def get_user_by_username(username:str, database=None) -> model.User:
    if 'person' not in database.list_collection_names():
        raise db_err.ItemDoesNotExistError(location=f'mongodb: Person at {DATABASE_NAME}@{HOST}:{PORT}', name=user_id)

    person_collection = database['person']
    person_as_dict = person_collection.find({'username':username})[0]

    return _user_from_mongo(person_as_dict)

@mongo_call_dec
def create_user(user:model.User, database=None) -> model.User:
    person_collection = database['person']

    # Check if person already exists
    if person_collection and person_collection.count_documents({'username':user.username}) > 0:
        raise db_err.ItemAlreadyExistError(location=f'mongodb: Person at {DATABASE_NAME}@{HOST}:{PORT}', name=user.username)
    
    user_as_dict = user.__dict__
    del user_as_dict['user_id']
    result = person_collection.insert_one(user_as_dict)

    return get_user_by_id(result.inserted_id)

def get_document_from_system(document:model.Document):
    return []