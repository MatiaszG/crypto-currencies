from django.shortcuts import render
import requests


def index(response):
    data = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethereum%2C%20bitcoin%2C%20cardano&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    processedData = []
    context = {}

    for cryptoCurrency in data:
        processedData.append(cryptoCurrency)
        
    context = {'currencies': processedData}
    return render(response, 'main/page.html', context)
