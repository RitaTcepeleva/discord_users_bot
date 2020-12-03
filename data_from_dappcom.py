from bs4 import BeautifulSoup
import requests
import json
import emoji

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

def get_price():
    response = requests.get('https://api.etherscan.io/api?module=gastracker&action=gasoracle')  # Get-запрос
    json_data = json.loads(response.text)  # Извлекаем JSON
    propose_gas_price = str('Gas (' + json_data['result']['ProposeGasPrice'] + ' Gwei)')
    status_price = emoji.emojize(':high_voltage:'+json_data['result']['FastGasPrice']+' | :turtle:'+json_data['result']['SafeGasPrice'])
    return propose_gas_price, status_price

def get_liq():
    web_req = requests.get('https://www.dextools.io/app/uniswap/pair-explorer/0x10db37f4d9b3bc32ae8303b46e6166f7e9652d28')
    content = BeautifulSoup(web_req.text, 'html.parser')
    assets = content.find_all('ul')

#print(get_liq())
