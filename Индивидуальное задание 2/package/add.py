#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_prod():
    name = input("Введите название для товара: ")
    shope = input("Введите название магазина:  ")
    price = float(input("Стоимость товара:  "))
    return {
        'name': name,
        'price': price,
        'shope': shope,
    }
