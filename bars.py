import json
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath) as json_file:
        data_dict = json.load(json_file)
    return data_dict


def get_biggest_bar(data):
    try:
        big_bar = max(data, key=lambda k: k['SeatsCount'])
        return big_bar['Name']
    except TypeError:
        pass

def get_smallest_bar(data):
    try:
        min_bar = min(data, key=lambda k: k['SeatsCount'])
        return min_bar['Name']
    except TypeError:
        pass

def get_closest_bar(data, longitude, latitude):
    try:
        for bar in data:
            bar['distance_key'] = calculation_euclidean_distance(float(bar['Longitude_WGS84']),
                                                                 float(bar['Latitude_WGS84'])
                                                                 , longitude, latitude)
        closest_bar = min(data, key=lambda k: k['distance_key'])
        return closest_bar['Name']
    except TypeError:
        pass


def calculation_euclidean_distance(longitude_json, latitude_json, longitude, latitude):
    try:
        distance = (((longitude_json-longitude)**2)+((latitude_json-latitude)**2))**0.5
        return distance
    except ValueError:
        pass


if __name__ == '__main__':
    file = input("Введите имя файла(путь к файлу) ")
    try:
        latitude = float(input('Введите широту: '))
        longitude = float(input("Введите longitude "))
    except ValueError:
        latitude = None
        longitude = None
    data_input = load_data(file)
    print("Самый большой бар = {0} \n"
          "Самый маленький бар = {1} \n"
          "Самый близкий бар = {2}".format(get_biggest_bar(data_input), get_smallest_bar(data_input),
                                           get_closest_bar(data_input, longitude, latitude)))
