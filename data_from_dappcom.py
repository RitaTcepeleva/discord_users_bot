from bs4 import BeautifulSoup
import requests
import json

def get_info():
    web_req = requests.get('https://www.dapp.com/app/rubic')
    content = BeautifulSoup(web_req.text, 'html.parser')
    assets = content.find_all('div', class_='sub-stats-item')
    users_24 = assets[1].contents[8].text
    total_uni_us = assets[1].contents[6].text
    assets = content.find_all('div', class_='balance')
    tvl = assets[0].contents[2].text.replace('\n                        ', ' ')
    assets = content.find_all('div', class_='contract')
    contracts = assets[0].contents[2].text+': '+assets[0].contents[0].text.replace('\xa0', '')
    str = users_24+'\n'+total_uni_us+'\n'+tvl+'\n'+contracts
    return str

#print(get_info())
