from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
# <---------directions setup and config lives above this line------>


# <------------------the plan--------->

# ____________________________________
# ____________________________________
# ____________________________________
# ____________________________________


# print each direction into this array =[]
# traversal_path=[]
#
# #
# maintain a visited {} with each room you go in
# visitedrooms={}
#
# #
# maintain a lastfork dict of arrays
# key is roomID of last fork
# value is and array of directions taken from that room
# you can reverse them in order of Last_In_1st_Out or a stack
# {12:[s,e,s,e,n,w],76:[s,s,e,e,n,w,w],24:[s,s,e,e,s,e,s]}#
#### lastfork= []
#### allforks=[] or {}
#
#
# #
# maintain a current room as the current room id
# currentroom=423
#
# #
# check each currentroom for neighbors
# #
# maintain a nextneighbors stack =[]
# nextneighbors=[]
#
# determine which way to go from the neighborsnumber and if they are new
#
# if no new neighbors go use the the lastfork=allforks[-1]
#  lastfork is a stack so you pop off each direction from it
# and go the opposite
# if its n you go s
# use a little reversing method
#
#
# check each new current room as you go  or no
#
# instead of going one room at a time.
# when you get to a room with no new neighbors
# look at the list of lastforks
# take the one at the end
# use a reversing method to  creatin a string that would both get you to the last fork if followed and can be append directly to the traversal path
#
# then append it to the traversal path
#
# next skip the room inbween they are already on the TraversalPath and if they had neighbors tehy would be the next last fork
#
# set currentroom to the id of lastfork
#
# get neigbors
# go into the neighbor that is not yet visited
# if all are visited go to nextlastfork again
#
# if you find newneighbros addd #
##
# #
# ____________________________________
# __________END__________________________
# ___________OF_________________________
# _________theplan__________________________
# ____________________________________

# <---------my code to find the traversal path lives below this line------>


# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = []
visitedrooms = {}
allforks = []
currentroom = 0
# stack of tuples (room.instance,room.dir,room.id) #
nextneighborstack = []

# direction we just came from
backtrack = {"n": "s", "s": "n", "e": "w", "w": "e"}
#
# there's a hangup with adding the found newneighbors to nextneighborsstack traversal_path and visited_rooms
# its adding the memorylocation unless i use '.id' on the end in which case i cant get the neighbors .
# we need the full Room aka sans -(.id) for getting neighbors aka compass direction
# and we need the number/id for the visited list
# maybe we should store them both as a keyvalue pair
# visited is a dict
# i think i need both the room instance and the id
# going to try storing the room.id as key and a tuple(roominstance,roomdir) as the value
# its a list
# so store all three as a triplet style tuple that way i can grab them off in order add like a stack
# # [-1]==(room.id,room.dir,room.instance)#

# getneighbors


def get_neighbors():
    return player.current_room.get_exits()



def dft(starting_vertex, visited={}):
    global traversal_path
    visited[player.current_room.id]=True
    newneighbors = {}
    newneighborscount = 0
    neighbors = get_neighbors()
    neighbors_length = len(neighbors)
    countednewneighbors=False
    if len(nextneighborstack) < 1 and newneighborscount is None and visited is not None:
        return visited
    for nbr in nextneighborstack:
        if nbr[0] in visited:
            nextneighborstack.remove(nbr)
    for nbr in neighbors:
        nbr_direction = nbr
        nbr_id = player.current_room.get_room_in_direction(nbr_direction).id
        if nbr_id not in visited:
            nextneighborstack.append((nbr_id, nbr_direction))
            newneighborscount += 1
        if nbr is neighbors[-1]:
            countednewneighbors=True
            

    if neighbors_length >= 3 and newneighborscount >= 1:
        next_room = nextneighborstack.pop()
        direction_to_travel = next_room[1]
        visited[next_room[0]] = next_room
        traversal_path += direction_to_travel
        allforks.append((player.current_room.id, [direction_to_travel]))
        player.travel(direction_to_travel)

        dft(player.current_room, visited)

    if newneighborscount == 1:

        if len(nextneighborstack) < 1:
            return
        next_room = nextneighborstack.pop()
        newneighborscount=0
        visited[next_room[0]] = next_room
        direction_to_travel = next_room[1]
        traversal_path += direction_to_travel
        allforks[-1][1].append(direction_to_travel)
        player.travel(direction_to_travel)
        dft(player.current_room, visited)

    if countednewneighbors==True and newneighborscount == 0:
        if len(allforks) == 0:
            return f' where is the mazeeee'
        else:
            breadcrumbs = allforks[-1][1]
            fork=allforks[-1][0]
            while len(breadcrumbs) != 0:
                breadcrumb = backtrack[breadcrumbs.pop()]
                traversal_path.append(breadcrumb)
                player.travel(breadcrumb)
            allforks.pop()
            dft(player.current_room, visited)

dft(world.starting_room,visited={})
# save thjem as a list
# loopthrough crntneighbors checking are they in visited
# add any new neighbors to newneighbors stack
# keep a count of new neighbors starting over in each room

#
# now
# depending on # of new neighbros found in this room
# if 1 continue
# if 0 turn around go to last fork and check neighbors again
#   for rm in lastfork[-1][2]:
#       if lastfork[-1][2] is not None:
#           player.travel(rm)
#           traversal_path.append(rm)
#           lastfork[-1][2].pop(-1)
#       else:
#           lastfork.pop()
#       #
# #
# if #


# def get_neighbors():
#     return player.current_room.get_exits()

# def dft(starting_vertex,visited={}):
#     global traversal_path
#     player.current_room=starting_vertex
#     neighbors=get_neighbors()
#     newneighbors={}
#     newneighborscount=0
#     neighbors_length=len(neighbors)

#     for neighbor in neighbors:
#         #
#         neighbor_direction=neighbor
#         # prints n, s, e, or w  #
#         # example => e          #
#         print(f'151 neighbor {neighbor}')
#         neighbor_instance=player.current_room.get_room_in_direction(neighbor)
#         neighbor_instance_str=str(neighbor_instance)
#         #printes room instance
#         # #154 str(neighbor_instance)>>>>
#         #-------------------
#         #
#         #Room 1
#         #
#         #   (3,6)
#         #
#         #Exits: [n, s]
#         #<<<<<<🧨line 154#
#         print(f'154 str(neighbor_instance)>>>>{str(neighbor_instance)}<<<<<<🧨line 154 {neighbor_instance_str}🧨')
#         # prints the int #
#         #  example => 3  #
#         print(f'157 neighbor_id={neighbor_instance.id}')
#         if neighbor_instance not in visited:
#             nextneighborstack.append((neighbor_instance_str,neighbor_instance.id,neighbor_direction))
#             # prints nextneighborstack[1,5,7,3] #
#             print(f'161 nextneighborstack{nextneighborstack}')
#             newneighborscount+=1
#             newneighbors[neighbor_instance.id]=neighbor_direction
#             #prints newneighbors{1: 'n', 5: 's', 7: 'w', 3: 'e'} #
#             print(f'165 newneighbors{newneighbors}')

#     if neighbors_length>=3 and newneighborscount>=1:
#         next_room=nextneighborstack.pop(-1)
#         print(f'line169 next_room {next_room}')
#         visited[next_room]=nextneighborstack
#         directiontotravel=newneighbors[next_room]
#         allforks.append((player.current_room.id,[directiontotravel]))
#         traversal_path += directiontotravel.__str__()
#         dft(next_room[0],visited)

#     if newneighborscount==1:
#         next_room=nextneighborstack.pop(-1)
#         visited[next_room]=nextneighborstack
#         directiontotravel=newneighbors[next_room]
#         allforks[-1][1].append(directiontotravel)
#         traversal_path=[*traversal_path,directiontotravel]
#         dft(next_room[0].__iter__(),visited,traversal_path)

#     return print(f'183 player.current_room|{player.current_room.id}|\n traversal_path| {traversal_path}|\n visited| {visited} | \n newneighbors | {newneighbors} |\n\n')


#     if newneighborscount==0:
#         if len(allforks) is None:
#             return f'wheres the maze dude'
#         else:
#             lastfork=allforks.pop(-1)
#             next_room=lastfork[0]
#             if next_room not in visited:
#                 visited[next_room]=nextneighborstack
#             walkbackwards=lastfork[1].reverse()
#             breadcrumbs=[backtrack[i] for i in walkbackwards]
#             traversal_path=[*traversal_path,*breadcrumbs]
#             dft(next_room,visited)


# dft(world.starting_room,visited={})
# print (f'201 traversal_path{traversal_path}')


# def get_neighbors():
#     return player.current_room.get_exits()
# def dft(starting_vertex,visited={}):
#     print(f'138 PLAYER.CURRENT_ROOM IS>>>>>>>{player.current_room} {type(player.current_room)}<🏉⚽🎱🎳🕺🏻')
#     print(f'139 starting_vertex IS>>>>>>>{starting_vertex}{type(starting_vertex)}')
#     global traversal_path
#     player.current_room=starting_vertex
#     neighbors=get_neighbors()
#     newneighbors={}
#     newneighborscount=0
#     neighbors_length=len(neighbors)
#     for neighbor in neighbors:
#         #
#         neighbor_direction=neighbor
#         # prints n, s, e, or w  #
#         # example => e          #
#         print(f'151 neighbor {neighbor}')
#         neighbor_instance=player.current_room.get_room_in_direction(neighbor)
#         neighbor_instance_str=str(neighbor_instance)
#         print(f'154 str(neighbor_instance)>>>>{str(neighbor_instance)}<<<<<<🧨line 154 {neighbor_instance_str}🧨')
#         # prints the int #
#         #  example => 3  #
#         print(f'157 neighbor_id={neighbor_instance.id}')
#         if neighbor_instance not in visited:
#             nextneighborstack.append((neighbor_instance_str,neighbor_instance.id,neighbor_direction))
#             # prints nextneighborstack[1,5,7,3] #
#             print(f'161 nextneighborstack{nextneighborstack}')
#             newneighborscount+=1
#             newneighbors[neighbor_instance.id]=neighbor_direction
#             #prints newneighbors{1: 'n', 5: 's', 7: 'w', 3: 'e'} #
#             print(f'165 newneighbors{newneighbors}')
#     if neighbors_length>=3 and newneighborscount>=1:
#         next_room=nextneighborstack.pop(-1)
#         print(f'line169 next_room {next_room}')
#         visited[next_room]=nextneighborstack
#         directiontotravel=newneighbors[next_room]
#         allforks.append((player.current_room.id,[directiontotravel]))
#         traversal_path += directiontotravel.__str__()
#         dft(next_room[0],visited)
#     if newneighborscount==1:
#         next_room=nextneighborstack.pop(-1)
#         visited[next_room]=nextneighborstack
#         directiontotravel=newneighbors[next_room]
#         allforks[-1][1].append(directiontotravel)
#         traversal_path=[*traversal_path,directiontotravel]
#         dft(next_room[0].__iter__(),visited,traversal_path)
#     return print(f'183 player.current_room|{player.current_room.id}|\n traversal_path| {traversal_path}|\n visited| {visited} | \n newneighbors | {newneighbors} |\n\n')
#     if newneighborscount==0:
#         if len(allforks) is None:
#             return f'wheres the maze dude'
#         else:
#             lastfork=allforks.pop(-1)
#             next_room=lastfork[0]
#             if next_room not in visited:
#                 visited[next_room]=nextneighborstack
#             walkbackwards=lastfork[1].reverse()
#             breadcrumbs=[backtrack[i] for i in walkbackwards]
#             traversal_path=[*traversal_path,*breadcrumbs]
#             dft(next_room,visited)
# dft(world.starting_room,visited={})
# print (f'201 traversal_path{traversal_path}')
# <---------my code to find the traversal path lives above this line------>
# <--------- test config lives down there below this line------>
# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
