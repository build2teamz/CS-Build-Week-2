from player import Player
import time 

player=Player('Reed', 0)
player.init()




traversalPath = []
print(traversalPath)
#-----------
copy={}
rooms={}
reverse=[]
#-----------
while len(copy) < 500 or player.currentRoom.title != 'Shop' or player.currentRoom.room_id == '0':
  cooldown=player.currentRoom['cooldown']
  time.sleep(cooldown)
  time.sleep(2)
  # if player.currentRoom['Shop']:
  #   print('you made it')
  #   break
  # else:
  #   next

  # if len(player.currentRoom['items'])> 0:
  #   player.take()
  #   print('if/take')
  #   next
  # else:
  #   print('else/take')
  #   next

  # time.sleep(2)
  print(player.currentRoom)
  # if len(player.currentRoom['items']) > 0:
  #   player.take()
  #   print('yay items')
  # else:
  #   next

  #   if player.currentRoom['title'] == 'Shop':
  #     player.sell()
  #   else:
  #     next


  current_room=player.currentRoom['room_id']
  if current_room not in copy:
    copy[current_room]=current_room
    exits={}
  
    for exit in player.currentRoom['exits']:
      exits[exit]="unknown"

    copy[current_room]=exits
  
  exits=copy[current_room]

  if current_room not in rooms:
      rooms[current_room]=current_room
      roomObj=player.currentRoom
      rooms[current_room]=roomObj
      
  # if 'w' in copy[current_room] and exits['w'] == 'unknown':
  #   if exits['w'] == 'unknown':
  #     player.travel("w")
  #     traversalPath.append("w")
  #     newRoom = player.currentRoom['room_id']
  #     exits['w'] = newRoom
  #     newExits = {}
  #     if newRoom not in copy:
  #       for exit in player.currentRoom['exits']:
  #         newExits[exit] = "unknown"
  #         copy[newRoom] = newExits
  #       newExits['e'] = current_room
  #     reverse.append('e')

  elif 'n' in copy[current_room] and exits['n'] == 'unknown':
    if exits['n']=='unknown':
      player.travel("n")
      traversalPath.append("n")
      newRoom=player.currentRoom['room_id']
      exits['n']=newRoom
      newExits={}
      if newRoom not in copy:
        for exit in player.currentRoom['exits']:
          newExits[exit]="unknown"
          copy[newRoom]=newExits
        newExits['s']=current_room
      reverse.append('s')

  elif 's' in copy[current_room] and exits['s'] == 'unknown':
    if exits['s']=='unknown':
      player.travel("s")
      traversalPath.append("s")
      newRoom=player.currentRoom['room_id']
      exits['s']=newRoom
      newExits={}
      if newRoom not in copy:
        for exit in player.currentRoom['exits']:
          newExits[exit]="unknown"
          copy[newRoom]=newExits
        newExits['n']=current_room
      reverse.append('n')

  elif 'e' in copy[current_room] and exits['e'] == 'unknown':
    if exits['e']=='unknown':
      player.travel("e")
      traversalPath.append("e")
      newRoom=player.currentRoom['room_id']
      exits['e']=newRoom
      newExits={}
      if newRoom not in copy:
        for exit in player.currentRoom['exits']:
          newExits[exit]="unknown"
          copy[newRoom]=newExits
        newExits['w']=current_room
      reverse.append('w')

  elif 'w' in copy[current_room] and exits['w'] == 'unknown':
    if exits['w']=='unknown':
      player.travel("w")
      traversalPath.append("w")
      newRoom=player.currentRoom['room_id']
      exits['w']=newRoom
      newExits={}
      if newRoom not in copy:
        for exit in player.currentRoom['exits']:
          newExits[exit]="unknown"
          copy[newRoom]=newExits
        newExits['e']=current_room
      reverse.append('e')

  else: 
    reversal=reverse.pop()
    player.travel(reversal)
    traversalPath.append(reversal)
