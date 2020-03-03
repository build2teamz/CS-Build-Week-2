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

    def init(self):
        response=requests.get(
            'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers=headers 
        )
        nextRoom=json.loads(response.text)
        self.currentRoom=nextRoom
        print(response.text)
