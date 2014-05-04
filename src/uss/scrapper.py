import requests
import json

SCRAPPER_URL = "http://api.embed.ly/1/oembed"

def scrapper(link_to_scrap):    
    scrapper_link = SCRAPPER_URL + '?url=' + link_to_scrap 
    response = requests.get(scrapper_link)
    return json.loads(response.content)