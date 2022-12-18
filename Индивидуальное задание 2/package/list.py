#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def list_1(products):
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 5,
        '-' * 20,
        '-' * 14,
        '-' * 17
    )
    print(line)
    print(
        '| {:^5} | {:^20} | {:^14} | {:^17} |'.format(
            "№",
            "Название товара",
            "Цена",
            "Название магазина"
        )
    )
    print(line)
    # Вывести данные о всех товарах.
    for idx, product in enumerate(products, 1):
        print(
            '| {:>5} | {:<20} | {:<14.2f} | {:>17} |'.format(
                idx,
                product.get('name', ''),
                product.get('price', 0),
                product.get('shope', '')
            )
        )
    print(line)
