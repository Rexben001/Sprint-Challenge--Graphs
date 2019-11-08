from room import Room
from player import Player
from world import World
from util import Stack, Queue
from graphRooms import roomGraph1, roomGraph2, roomGraph3, roomGraph4, roomGraph5

import random

# Load world
world = World()

# All roomGraphs
# roomGraph = roomGraph1
# roomGraph = roomGraph2
# roomGraph = roomGraph3
# roomGraph = roomGraph4
roomGraph = roomGraph5

# Fill this out
traversalPath = []


def checkAllRooms(roomID):
    for room in roomGraph[roomID][1].values():
        # print('RS', room, enteredRooms)
        if room not in enteredRooms:
            return True
    return False


def enterFirstRoom(roomID):
    for direction, room in roomGraph[roomID][1].items():
        # print('DR', direction, room)
        if room not in enteredRooms:
            traversalPath.append(direction)
            enteredRooms.add(room)
            return room

# Use dft


def goBack():
    visited = set()
    paths = {}
    s = Stack()
    s.push(currentRoom)
    paths[currentRoom] = [currentRoom]
    while s.size() > 0:
        room = s.pop()
        visited.add(room)
        for rm in roomGraph[room][1].values():
            if rm not in visited:
                copiedPath = paths[room].copy()
                # print('NP', paths)
                copiedPath.append(rm)
                paths[rm] = copiedPath
                if checkAllRooms(rm):
                    newPath = paths[rm]
                    # print('CP', newPath)
                    directions = []
                    for i in range(len(newPath) - 1):
                        for d, r in roomGraph[newPath[i]][1].items():
                            value = d if r == newPath[i + 1] else None
                            directions.append(value)
                        enteredRooms.add(newPath[i + 1])
                    return (directions, newPath[len(newPath) - 1])
                s.push(rm)
    return None


world.loadGraph(roomGraph)

world.printRooms()

player = Player("Name", world.startingRoom)

traversalPath = []

enteredRooms = set()
enteredRooms.add(0)
currentRoom = 0
while True:
    while checkAllRooms(currentRoom):
        currentRoom = enterFirstRoom(currentRoom)
    tracedValues = goBack()
    if tracedValues:
        newPath = tracedValues[0]
        traversalPath.extend(newPath)
        currentRoom = tracedValues[1]
    else:
        break


# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)

for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

# print('v', len(visited_rooms))
# print('g', len(roomGraph))

if len(visited_rooms) == len(roomGraph):
    print(
        f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")

