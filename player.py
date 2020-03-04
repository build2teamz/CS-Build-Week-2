import requests
import json
import time

auth_key = 'Token 48ccfedba933f858b05ceefb8390e4cb9d99b109'

headers = {
    'Authorization': auth_key,
    'Content-Type': 'application/json'
}

class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom
        # startingRoom = 55
    def travel(self, direction):
        if direction == "n":
            data={"direction": "n"}
        if direction == "s":
            data={"direction": "s"}
        if direction == "e":
            data={"direction": "e"}
        if direction == "w":
            data={"direction": "w"}
        response=requests.post(
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/move/', headers=headers, data=json.dumps(data)
        )

        nextRoom=json.loads(response.text)
        self.currentRoom=nextRoom
    def take(self):
        if len(self.currentRoom['items']) > 0:
            data = {'name': 'treasure'}
        response = requests.post(
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/take/', headers=headers, data=json.dumps(data)
        )
        nextRoom = json.loads(response.text)
        self.currentRoom = nextRoom
    def init(self):
        response=requests.get(
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers 
        )
        nextRoom=json.loads(response.text)
        self.currentRoom=nextRoom
<<<<<<< HEAD
        print(response.text)
=======

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
>>>>>>> 8b470f22b27e0dff3979bb1b401c94c78384beb7
