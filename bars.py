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
    maxim = data[i]['SeatsCount']
    while i < len(data):
        if data[i]['SeatsCount']>maxim:
            maxim = data[i]['SeatsCount']
            name_bar = data[i]['Name']
        i += 1
    print(name_bar)


def get_smallest_bar(data):
    data = load_data('data.json')
    i = 0
    minim = data[i]['SeatsCount']
    while i < len(data):
        if data[i]['SeatsCount']<minim:
            minim = data[i]['SeatsCount']
            name_bar = data[i]['Name']
        i += 1
    print(name_bar)


def get_closest_bar(data, longitude, latitude):
    data = load_data(data)
    i = 0
    ids = 0
    min_euql = 50
    while i < len(data):
        a = euqlid(float(data[i]['Longitude_WGS84']), float(data[i]['Latitude_WGS84']), longitude, latitude)
        if a < min_euql:
            min_euql = a
            ids = data[i]['global_id']
            name_bar = data[i]['Name']
        i += 1
    print(name_bar)


def euqlid(longitude, latitude, x1, y1):
    d = math.sqrt(math.pow((longitude-x1), 2)+math.pow((latitude-y1), 2))
    return d


long = float(input("Введите долготу "))
lat = float(input("Введите ширину "))

get_biggest_bar('data.json')
get_smallest_bar('data.json')
get_closest_bar('data.json', long, lat)
if __name__ == '__main__':
    pass
