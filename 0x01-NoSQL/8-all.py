#!/usr/bin/env python3
'''
8. List all documents in Pyfrom
'''
'''
from pymongo import mongoclient
'''
from typing import List


def list_all(mongo_collection) -> List:
    '''
    a Python function that lists all documents in a collection:

    Prototype: def list_all(mongo_collection):
        Return an empty list if no document in the collection
        mongo_collection will be the pymongo collection object
    '''
    result = [data for data in mongo_collection.find() if data]

    return result
