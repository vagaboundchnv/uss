import requests
import json

SCRAPPER_URL = "http://api.embed.ly/1/oembed"

def scrapper(url):    
    link_to_scrap = SCRAPPER_URL + '?url='+ url['link']
    response = requests.get(link_to_scrap)
    return json.loads(response.content)