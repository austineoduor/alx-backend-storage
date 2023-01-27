#!/usr/bin/env python3
'''
9. Insert a document in Python
'''


def insert_school(mongo_collection, **kwargs):
    '''
    a Python function that inserts a new document in a collection
    based on kwargs:

    Prototype: def insert_school(mongo_collection, **kwargs):
        mongo_collection will be the pymongo collection object
        Returns the new _id
    '''
    result = mongo_collection.insert_one(kwargs)
    _id = result.inserted_id 
    return _id
