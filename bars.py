# -*- coding: utf-8 -*-
import json


def load_data(filepath):
    data_dict = {}
    with open(filepath) as json_file:
        data_dict = json.load(json_file)
    return data_dict


def get_biggest_bar(data):
    big_bar = sorted(data, key=lambda k: k['SeatsCount'], reverse=True)
    print(big_bar[0]['Name'])


def get_smallest_bar(data):
    min_bar = sorted(data, key=lambda k: k['SeatsCount'])
    print(min_bar[0]['Name'])


def get_closest_bar(data, longitude, latitude):
    for bar in data:
        bar['distance_key'] = euqlid(float(bar['Longitude_WGS84']), float(bar['Latitude_WGS84']), longitude, latitude)
    closest_bar = sorted(data, key=lambda k: k['distance_key'])
    print(closest_bar[0]['Name'])


def euqlid(longitude, latitude, x1, y1):
    d = (((longitude-x1)**2)+((latitude-y1)**2))**0.5
    return d


long = float(input("Введите долготу "))
lat = float(input("Введите ширину "))
data_input = load_data('data.json')
get_biggest_bar(data_input)
get_smallest_bar(data_input)
get_closest_bar(data_input, long, lat)
if __name__ == '__main__':
    pass
