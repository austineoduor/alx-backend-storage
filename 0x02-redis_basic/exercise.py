#!/usr/bin/env python3
'''
0. Writing strings to Redis
'''
import redis
from uuid import uuid4
from typing import Union, Optional, Callable


class Cache():
    '''
    a Cache class.
    '''
    def __init__(self) -> None:
        '''
        In the __init__ method,
        store an instance of the Redis client as
        a private variable named
        _redis (using redis.Redis()) and flush
        the instance using flushdb.
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        a store method that takes a data argument
        and returns a string. The method should generate
        a random key (e.g. using uuid), store the input
        data in Redis using the random key and return the key.

        Remember that data can be a str, bytes, int or float.
        '''
        userid = str(uuid4())
        self._redis.set(userid, data)
        return userid

    def get(self, key: str, fn: Optional[Callable] = None):
        '''
        a get method that take a key string argument and an
        optional Callable argument named fn.
        This callable will be used to convert the data back
        to the desired format.
        '''
        info = self._redis.get(key)
        return info if not fn else fn(info)

    def get_str(self, key: str) -> str:
        '''
        parametrize Cache.get with the correct conversion function
        '''
        r = self._redis.get(key)
        return r.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ automatically parametrize Cache.get to int """
        data = self._redis.get(key)
        try:
            data = int(value.decode("utf-8"))
        except Exception:
            data = 0
        return data
