#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from modul import outer


if __name__ == "__main__":
    ma = outer(1)
    print(ma([1, 2, 3, 4, -5]))
    mi = outer(-1)
    print(mi([1, 2, 3, 4, -5]))
