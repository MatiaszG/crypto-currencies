import json
from channels.generic.websocket import WebsocketConsumer
import requests


class Consumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': ['bitcoin', 'ethereum', 'cardano']
        }))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        data = requests.get(
            'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Ccardano&vs_currencies=usd').json()
        if message == "REFRESH":
            self.send(text_data=json.dumps({
                'type': 'REFRESH',
                'message': data
            }))
