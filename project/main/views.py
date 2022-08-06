from django.shortcuts import render
import requests


def index(response):
    data = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethereum%2C%20bitcoin%2C%20cardano&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()

    context = {'currencies': data}
    return render(response, 'main/page.html', context)


def exchanges(response):
    currencies = ['Bitcoin', 'Ethereum', 'Ripple', 'USD']
    if response.method == 'GET':
        context = {'currencies': currencies}
        return render(response, 'main/exchanges.html', context)
    elif response.method == 'POST':
        decrypter = {'Bitcoin': 'btc', 'Ethereum': 'eth',
                     'Ripple': 'xrp', 'USD': 'usd'}
        currency1 = response.POST['currency1']
        currency2 = response.POST['currency2']
        number = float(response.POST['number'])

        currencies_list1 = currencies.copy()
        currencies_list2 = currencies.copy()
        currencies_list1.remove(currency1)
        currencies_list1.insert(0, currency1)
        currencies_list2.remove(currency2)
        currencies_list2.insert(0, currency2)

        if(currency1 != 'USD'):
            price_data = requests.get(
                'https://api.coingecko.com/api/v3/coins/'+currency1[0].lower()+response.POST['currency1'][1:]+'?localization=flase&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false').json()['market_data']['current_price']
            price = price_data[decrypter[currency2]]
        elif(currency1 == 'USD' and currency2 != 'USD'):
            price_data = requests.get(
                'https://api.coingecko.com/api/v3/coins/'+currency2[0].lower()+response.POST['currency2'][1:]+'?localization=flase&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false').json()['market_data']['current_price']
            price = 1/price_data['usd']
        elif(currency1 == 'USD' and currency2 == 'USD'):
            price = 1
        price *= number

        context = {'currencies_list1': currencies_list1, 'currencies_list2': currencies_list2, 'price': price,
                   'currency1': decrypter[currency1].upper(), 'currency2': decrypter[currency2].upper(), 'number': number}
        return render(response, 'main/exchanges.html', context)
