import requests
import json
import time

auth_key = 'Token  6a9b68c63aadf1ed3cf49e3772a8567368423f0e'

headers = {
    'Authorization': auth_key,
    'Content-Type': 'application/json'
}


class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom

    def travel(self, direction):
        if direction == "n":
            data = {"direction": "n"}
        if direction == "s":
            data = {"direction": "s"}
        if direction == "e":
            data = {"direction": "e"}
        if direction == "w":
            data = {"direction": "w"}
        response = requests.post(
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, data=json.dumps(data)
        )

        nextRoom = json.loads(response.text)
        self.currentRoom = nextRoom

    def init(self):
        response = requests.get(
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers
        )
        nextRoom = json.loads(response.text)
        self.currentRoom = nextRoom
        print(response.text)

    def take(self):
        if len(self.currentRoom['items']) > 0:
            data = {'name': 'treasure'}
            response = requests.post(
                'https://lambda-treasure-hunt.herokuapp.com/api/adv/take/', headers=headers, data=json.dumps(data)
            )
        else:
            next

    def sell(self):
        if self.currentRoom['title'] == "Shop":
            data = {'name': 'treasure', 'confirm': 'yes'}
            response = requests.post(
                'https://lambda-treasure-hunt.herokuapp.com/api/adv/sell/', headers=headers, data=json.dumps(data)
            )
            print('Selling!')
        else:
            next
