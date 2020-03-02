class Player:
  def __init__(self, name, startingRoom):
    self.name = name
    self.currentRoom = startingRoom
    self.cooldown = 1
    self.encumbrance = 0
    self.strength = 0
    self.speed = 0
    self.gold = 0
    self.inventory = []
    self.status = []
    self.errors = []
    self.messages = []
    self.mine = ""