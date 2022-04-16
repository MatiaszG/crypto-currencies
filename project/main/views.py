from django.shortcuts import render
from django.shortcuts import redirect
import requests
from datetime import datetime


def index(response):
    data = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethereum%2C%20bitcoin%2C%20cardano&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    processedData = []
    context = {}
    for cryptoCurrency in data:
        chartData = requests.get('https://api.coingecko.com/api/v3/coins/' +
                                 cryptoCurrency['id']+'/market_chart?vs_currency=usd&days=10&interval=daily').json()
        priceData = chartData['prices']
        x = []
        y = []
        dates = []
        for arr in priceData:
            dates.append(datetime.fromtimestamp(arr[0]/1000).strftime('%m/%d'))
            x.append(arr[0])
            y.append(arr[1])
        processedData.append(cryptoCurrency)
    context = {'currencies': processedData}
    return render(response, 'main/page.html', context)
