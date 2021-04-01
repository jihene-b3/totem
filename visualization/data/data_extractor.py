import urllib.request
import json
import data.splitter


def __parse_to_json_array(string_to_parse):
    result = []
    for s in data.splitter.split(string_to_parse):
        result.append(json.loads(s))
    return result


def __extract_data_from_json_object(json_object, keys):
    result = {}
    for key in keys:
        result[key] = json_object[key]
    return result


def __extract_data_from_json_array(json_array, keys):
    result = []
    for json_object in json_array:
        result.append(__extract_data_from_json_object(json_object, keys))
    return result


def __extract_data_from_content(content, keys):
    json_array = __parse_to_json_array(content)
    return __extract_data_from_json_array(json_array, keys)


def extract_data_from_file(path, *keys):
    file = open(path)
    content = file.read().decode('utf-8')
    return __extract_data_from_content(content)


def extract_data_from_url(url, *keys):
    file = urllib.request.urlopen(url)
    content = file.read().decode('utf-8')
    return __extract_data_from_content(content, keys)
