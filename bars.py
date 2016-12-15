# -*- coding: utf-8 -*-
# import os
import json
import math


def load_data(filepath):

    # Создаем переменную для хранения
    data_dict = {}
    # открываем файл который передается параметром filepath
    with open(filepath) as json_file:
        # заполняем переменную data_dict
        data_dict = json.load(json_file)
    # возвращаем весь словарь
    return data_dict


def get_biggest_bar(data):
    data = load_data('data.json')
    i = 0
    minim = data[i]['SeatsCount']
    maxim = data[i]['SeatsCount']
    while i < len(data):
        if data[i]['SeatsCount']>maxim:
            maxim = data[i]['SeatsCount']
        i += 1
    print(maxim)


def get_smallest_bar(data):
    data = load_data('data.json')
    i = 0
    minim = data[i]['SeatsCount']
    while i < len(data):
        if data[i]['SeatsCount']<minim:
            minim = data[i]['SeatsCount']
        i += 1
    print(minim)


def get_closest_bar(data, longitude, latitude):
    data = load_data('data.json')


def euqlid(longitude, latitude):
    x1 = float(input())
    y1 = float(input())
    d = math.sqrt(math.pow((longitude-x1),2)+math.pow((latitude-y1),2))
    print(d)


long = 37.6215879462381080
lat = 55.7653669567739740
euqlid(long, lat)
# get_biggest_bar('data.json')
# get_smallest_bar('data.json')
if __name__ == '__main__':
    pass
