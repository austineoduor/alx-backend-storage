#!/usr/bin/env python3
'''Top students'''
from typing import List, Dict, Union


def top_students(mongo_collection) -> List[Dict[str, Union[str, int]]]:
    '''
    a Python function that returns all students sorted by average score:
        Prototype: def top_students(mongo_collection):
            mongo_collection will be the pymongo collection object
            The top must be ordered
            The average score must be part of each item returns with
            key = averageScore
    '''
    n = mongo_collection

    student_db = list(n.find())

    sort = []
    for data in student_db:
        '''
        getting data of students
        '''
        scores = [y.get('score') for y in data.get('topics')]

        sort.append({
            'name': data.get('name'),
            '_id': data.get('_id'),
            'averageScore': sum(scores) / len(scores)
            })

    return sorted(sort, key=lambda k: k['averageScore'], reverse=True)
