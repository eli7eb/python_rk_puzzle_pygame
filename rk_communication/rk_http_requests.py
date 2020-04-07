import requests
import json

rk_api_token = 'aTcoXoCh'
rk_url_postfix = '&q='
search_value = 'cat'
format_json = 'json'
rk_type_paint = 'painting'
rk_type_material = 'canvas'
rk_url_call_end = '\''
rk_api_url_base_prefix = 'https://www.rijksmuseum.nl/api/en/collection?key='+rk_api_token
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(rk_api_token)}
to_search = rk_url_postfix+search_value+format_json+rk_type_paint+rk_type_material

querystring = {"q": search_value, "format": format_json, "object_type": rk_type_paint, "material": rk_type_material}


response = requests.request("GET", rk_api_url_base_prefix, headers=headers, params=querystring)
if response.status_code == 200:
    print('success')
    print(response.text)

    json_obj = json.loads(response.content.decode('utf-8'))
    print(json_obj['artObjects'])
    print(json_obj)
else:
    print('error '+response.status_code)