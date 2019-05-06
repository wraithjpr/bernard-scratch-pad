#!/usr/bin/env python3
import functools

def hello(subject):
    print("hello, " + subject)

hello("world")

def call(fxn, param):
    fxn(param)

call(hello, "world")

def call_curried(fxn):
    return  functools.partial(call, fxn)

call_hello = call_curried(hello)

call_hello("world")

