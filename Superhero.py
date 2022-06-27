import requests

from pprint import pprint

list_of_heroes = ['Hulk', 'Captain America', 'Thanos']

def test_request():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url).json()
    return(response)


def smart_superhero(some_list):
    work_list = test_request()
    some_dict = {}
    for i in some_list:
        for b in work_list:
            if i == b['name']:
                some_dict[i] = b['powerstats']['intelligence']
    print(max(some_dict, key=some_dict.get))

smart_superhero(list_of_heroes)