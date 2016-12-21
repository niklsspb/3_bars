import json
import os


def load_data(path_to_file):
    if not os.path.exists(path_to_file):
        return None
    with open(path_to_file) as json_file:
        data_dictionary = json.load(json_file)
    return data_dictionary


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
            bar['distance_key'] = calculate_the_euclidean_distance(float(bar['Longitude_WGS84']),
                                                                 float(bar['Latitude_WGS84'])
                                                                 , longitude, latitude)
        closest_bar = min(data, key=lambda k: k['distance_key'])
        return closest_bar['Name']
    except TypeError:
        pass


def calculate_the_euclidean_distance(longitude_json, latitude_json, input_user_longitude, input_user_latitude):
    try:
        distance = (((longitude_json-input_user_longitude)**2)+((latitude_json-input_user_latitude)**2))**0.5
        return distance
    except ValueError:
        pass


if __name__ == '__main__':
    input_file_name = input("Введите имя файла(путь к файлу) ")
    try:
        latitude = float(input('Введите latitude : '))
        longitude = float(input("Введите longitude "))
    except ValueError:
        latitude = None
        longitude = None
    data_input = load_data(input_file_name)
    print("Самый большой бар = {0} \n"
          "Самый маленький бар = {1} \n"
          "Самый близкий бар = {2}".format(get_biggest_bar(data_input), get_smallest_bar(data_input),
                                           get_closest_bar(data_input, longitude, latitude)))
