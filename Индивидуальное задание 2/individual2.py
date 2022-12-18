#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from package.add import get_prod
from package.list import list_1
from package.select import select
from package.help_1 import help_1


def main():
    print("help - список всех команд")
    products = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == "add":
            product = get_prod()

            products.append(product)
            products.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            list_1(products)

        elif command == 'select':
            select(products)

        elif command == "help":
            help_1()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
