from decouple import config
from util import Stack, Queue
from ast import literal_eval
import random
import requests
import json
'''
# Load world
world = World()



# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
'''

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# Keeps track of route the player took
traversal_path = []
visited = {}

# Starting room as per the readme
beginning_room = {'n': '?', 's': '?', 'w': '?', 'e': '?'}
# The player begins in room '0'
visited[0] = beginning_room
# Useing a bfs that looks for a '?'
auth_key = config('AUTH_KEY')

# keeps track of what rooms the player has visited

class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.cooldown = 0
        self.inventory = []
        self.player_errors = []
        self.player_messages = []


class Search_Map:
    def __init__(self, auth_token = auth_key):
        self.auth_token = auth_token
        self.header = {'Authorization': f'Token {self.auth_token}'}

    def move_options(self, command,  direction = None):
        if command == 'init':
            response = requests.get(
                f'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers = self.header)
    def bfs_map(starting_vertex):
        # create an empty queue
        queue = Queue()
        # Create an empty set to store visited rooms
        bfs_visited = set()
        # Add a path to the starting vertex_id to the queue
        queue.enqueue([starting_vertex])
        # While the queue is not empty...
        while queue.size() > 0:
            # dequeue, the first path
            path = queue.dequeue()
            # Grab the last rom from the path
            room_vertex = path[-1]
            # If room is not in bfs_visited
            if room_vertex not in bfs_visited:
                # Check if its reached a target of '?'
                for room in visited[room_vertex]:
                    # Check if the set has the current room and that room has unexplored exits
                    if visited[room_vertex][room] == '?':
                        # If it finds an unexplored exit, break the loop and return the path to it
                        return path
                # Mark it as visited
                bfs_visited.add(room_vertex)
                # then add a path to all neighbors to the back of the queue
                for neighbor in visited[room_vertex]:
                    # Make a copy of the path
                    path_copy = list(path)
                    # append the path copy with neighbor
                    path_copy.append(visited[room_vertex][neighbor])
                    # Add the path copy to the queue
                    queue.enqueue(path_copy)
        # If no destination was found return None
        return None

    # Finds a possible route to travel down


    def travel_route(route):
        # all the possible exits for a room
        exit_list = []
        # Cycle through each room in the route being passed in
        for room in route:
            # Find how many exits each room has
            for exit in visited[route[0]]:
                # Check if the room and the exit for the first visited room are a match
                if room == visited[route[0]][exit]:
                    # Add the exit to the list
                    exit_list.append(exit)
        # Return a list of exits for the room
        return exit_list

    # Simple if else function for the inverse of each direction so the player can backtrack the route


    def backtrack_route(direction):
        # Initialize a variable to store the backtracked direction
        reverse_direction = None
        if direction == 'n':
            reverse_direction == 's'
        elif direction == 's':
            reverse_direction == 'n'
        elif direction == 'w':
            reverse_direction == 'e'
        elif direction == 'e':
            reverse_direction == 'w'
        # Return the new direction
        return reverse_direction


    # While loop that runs until it hits a 'break'
    while True:
        # Variable for just finding the location id of where the player is
        current_room = visited[player.current_room.id]
        # List of exits in each room
        room_list = []
        # Cycle through the current room exits
        for next_room in current_room:
            # Check if there are any unexplored exits
            if current_room[next_room] == '?':
                # Add the unexplored room directions to the room exit list
                room_list.append(next_room)
        # Check if a room has at least 1 unexplored direction
        if len(room_list) > 0:
            # Randomely choose a direction to travel in
            random.shuffle(room_list)
            # Set a direction to travel down based on the list of shuffled rooms
            travel_direction = room_list[0]
            # Use a variable that can be used for the backtrack_route function
            previous_room = visited[player.current_room.id]
            # The id of the previous room
            previous_room_id = player.current_room.id
            # Add the direction to the path for the player to travel
            traversal_path.append(travel_direction)
            # Use the travel method to actually move the direction
            player.travel(travel_direction)
            # Create a set to store the exits for an uneplored room
            set_exits = {}
            # Check if the player is currently in a room that is not been visited
            if player.current_room.id not in visited:
                # Find all the exits in a non-visited room
                for direction in player.current_room.get_exits():
                    # Update the exits in the room to a '?' so it can be explored
                    set_exits.update({direction: '?'})
                # Update the room to have the exits that need to be explored
                visited[player.current_room.id] = set_exits
            # Start juggleing the room ids so the algo can go back to keep exploring rooms
            previous_room[travel_direction] = player.current_room.id
            # Set the direction to backtrack once it has explored a path
            backtrack = backtrack_route(travel_direction)
            # Update the visited set to reflect all the room's exits
            visited[player.current_room.id][backtrack] = previous_room_id
        # Else the player has hit a dead end
        else:
            # Set a variable that starts the bfs to find a new destination to search for
            get_route = bfs_map(player.current_room.id)
            # If there are still valid paths to travel
            if get_route is not None:
                # A variable for storing the route with new direction
                directions = travel_route(get_route)
                # loop through all the directions in the route
                for direction in directions:
                    # Make a new traversal path with the directions
                    traversal_path.append(direction)
                    # Move the player in the direction
                    player.travel(direction)
            # If all the rooms have been explored than bfs return None so break the while loop
            if get_route == None:
                break
