import requests
import json
from random import randrange

class SearchArt:

    def getImageList(self):
        rk_api_token = 'aTcoXoCh'
        rk_url_postfix = '&q='

        format_json = 'json'
        rk_type_paint = 'painting'
        rk_type_material = 'canvas'
        rk_url_call_end = '\''
        rk_api_url_base_prefix = 'https://www.rijksmuseum.nl/api/en/collection?key=' + rk_api_token
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {0}'.format(rk_api_token)}

        query_params = {"q": self.search_value, "format": format_json, "object_type": rk_type_paint,
                       "material": rk_type_material}

        response = requests.request("GET", rk_api_url_base_prefix, headers=headers, params=query_params)
        if response.status_code == 200:
            print('success')
            print(response.text)

            json_obj = json.loads(response.content.decode('utf-8'))
            print(json_obj['artObjects'])
            art_list = json_obj['artObjects']

            if len(art_list) > 0:
                art_index = randrange(len(art_list))
            print(art_index)
            return art_list[art_index]
        else:
            print('error ' + response.status_code)

    def __init__(self, mood_str):
        self.currentState = None
        self.search_value = mood_str

class GetArtWork:
    print('get the one')

    def __init__(self, art_dict):
        self.currentState = None
        self.art_dict = art_dict

    def getArtImage(self):
        rk_api_token = 'aTcoXoCh'
        rk_url_postfix = '&q='
        # get random of list
        # String prefix = "https://www.rijksmuseum.nl/api/en/collection/"+params[0].get_object_number()+"/tiles?format=json&key=";
        format_json = 'json'
        object_number = self.art_dict.get("objectNumber","")
        rk_type_paint = 'painting'
        rk_type_material = 'canvas'
        rk_url_call_end = '\''
        rk_api_url_base_prefix = 'https://www.rijksmuseum.nl/api/en/collection/'+object_number+'/tiles'+'?key=' + rk_api_token
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {0}'.format(rk_api_token)}

        query_params = { "format": format_json }

        response = requests.request("GET", rk_api_url_base_prefix, headers=headers, params=query_params)
        if response.status_code == 200:
            print('success')
            print(response.text)
            json_obj = json.loads(response.content.decode('utf-8'))
            print(json_obj)
        else:
            print ('error '+response.status_code + ' '+response.text)