#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def outer(t):
    def inner(arr):
        if t == 1:
            return max(arr)
        else:
            return min(arr)

    return inner
