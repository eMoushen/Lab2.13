#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def select(products):
    # Проверить наличие товара.
    nalich = "new balance"

    flag = False
    for product in products:
        if nalich in product['name']:
            print(f'Товар в наличии: {product["name"]}\nЦена: {product["price"]:.2f}\n')
            flag = True

    if not flag:
        print(f'\nТаких товаров нет: {nalich}')
