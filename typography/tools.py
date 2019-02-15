import json


def json_to_dict(file_name):
    json1_file = open(file_name, encoding='utf-8')
    json1_str = json1_file.read()
    json1_data = json.loads(json1_str)
    return json1_data


def format_key(key):
    key = key.lower()
    key = '_'.join(key.split(' '))
    return key
