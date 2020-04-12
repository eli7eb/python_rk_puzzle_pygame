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

        to_search = rk_url_postfix + self.search_value + format_json + rk_type_paint + rk_type_material

        querystring = {"q": self.search_value, "format": format_json, "object_type": rk_type_paint,
                       "material": rk_type_material}

        response = requests.request("GET", rk_api_url_base_prefix, headers=headers, params=querystring)
        if response.status_code == 200:
            print('success')
            print(response.text)

            json_obj = json.loads(response.content.decode('utf-8'))
            print(json_obj['artObjects'])
            art_list = json_obj['artObjects']
            print(json_obj)
        else:
            print('error ' + response.status_code)

        if len(art_list) > 0:
            art_index = randrange(len(art_list))

# get random of list
# String prefix = "https://www.rijksmuseum.nl/api/en/collection/"+params[0].get_object_number()+"/tiles?format=json&key=";
    #

    def __init__(self, mood_str):
        self.currentState = None
        self.search_value = mood_str
        self.getImageList()



class GetOneArtWork:
    print('get the one')