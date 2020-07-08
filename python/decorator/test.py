#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def dashes(func):
    def inner(*args, **kvargs):
        print("-" * 30)
        print(func(*args, **kvargs))
        print("-" * 30)
    return inner


@dashes
def helloWorld(msg):
    pass #print(msg)
    return msg


helloWorld("Hey!")
#dashes(helloWorld())