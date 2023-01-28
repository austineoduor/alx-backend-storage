#!/usr/bin/env python3
'''
12. Log stats
'''
from pymongo import MongoClient
from typing import List


def get_doc_count(conn) -> int:
    '''
    returns document count
    '''
    x = conn.count_documents({})
    return x


def get_method_count(conn) -> None:
    '''
    return method in method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    '''
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for i in method:
        '''print("\tmethod {}: {}".format(i, len(list(
            conn.find({"method": i})))))
        '''
        j = conn.count_documents({"method": i})
        print("\tmethod {}: {}".format(i, j))

def method_path(conn) -> int:
    '''
    one line with the number of documents with:
        method=GET
        path=/status
    '''
    y = conn.count_documents({"method": "GET", "path": "/status"})
    return y


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    conn = client.logs.nginx

    print("{} logs".format(get_doc_count(conn)))
    print("Methods:")
    get_method_count(conn)
    print("{} status check".format(method_path(conn)))
