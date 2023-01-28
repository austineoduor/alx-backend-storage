#!/usb/bin/env python3
'''
11. Where can I learn Python
'''
from typing import List


def schools_by_topic(mongo_collection, topic) -> List:
    '''
    a Python function that returns the list of school having a
    specific topic:

    Prototype: def schools_by_topic(mongo_collection, topic):
        mongo_collection will be the pymongo collection object
        topic (string) will be topic searched
    '''
    lists = [r for r in mongo_collection.find({"topics": topic})]
    return lists
