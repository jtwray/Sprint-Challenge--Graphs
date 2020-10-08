from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
## <---------directions setup and config lives above this line------>


##<------------------the plan--------->

# ____________________________________
# ____________________________________
# ____________________________________
# ____________________________________






##print each direction into this array =[]
### traversal_path=[]
# 
# #
##maintain a visited {} with each room you go in
### visitedrooms={}
# 
# #
##maintain a lastfork dict of arrays
# key is roomID of last fork
# value is and array of directions taken from that room
# you can reverse them in order of Last_In_1st_Out or a stack
# {12:[s,e,s,e,n,w],76:[s,s,e,e,n,w,w],24:[s,s,e,e,s,e,s]}#
#### lastfork= []
#### allforks=[] or {}
# 
# 
# #
##maintain a current room as the current room id
### currentroom=423
# 
# #
#check each currentroom for neighbors
# #
##maintain a nextneighbors stack =[] 
###nextneighbors=[] 
# 
# determine which way to go from the neighborsnumber and if they are new
# 
# if no new neighbors go use the the lastfork=allforks[-1]
#  lastfork is a stack so you pop off each direction from it 
# and go the opposite 
#if its n you go s
#use a little reversing method
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

## <---------my code to find the traversal path lives below this line------>




# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path=[]
visitedrooms={}
allforks=[]
currentroom=0
nextneighborstack=[]


#direction we just came from
backtrack={"n":"s","s":"n","e":"w","w":"e"}
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
# [-1]==(room.id,room.dir,room.instance)#
def get_neighbors():
    return player.current_room.get_exits()

def dft(starting_vertex,visited={}):
    print(f'PLAYER.CURRENT_ROOM IS>>>>>>>{player.current_room}')
    print(f'starting_vertex IS>>>>>>>{starting_vertex}{type(starting_vertex)}')
    global traversal_path
    player.current_room=starting_vertex
    neighbors=get_neighbors()
    newneighbors={}
    newneighborscount=0
    neighbors_length=len(neighbors)
    for neighbor in neighbors:
        #
        neighbor_direction=neighbor
        # prints n, s, e, or w  #
        # example => e          #
        print(f'neighbor{neighbor}')
        neighbor_id=player.current_room.get_room_in_direction(neighbor).id
        # prints the int #
        #  example => 3  #
        print(f'neighbor_id={neighbor_id}')
        if neighbor_id not in visited:
            nextneighborstack.append(neighbor_id)
            # prints nextneighborstack[1,5,7,3] #
            print(f'nextneighborstack{nextneighborstack}')
            newneighborscount+=1
            newneighbors[neighbor_id]=neighbor
            #prints newneighbors{1: 'n', 5: 's', 7: 'w', 3: 'e'} #
            print(f'newneighbors{newneighbors}')

    if neighbors_length>=3 and newneighborscount>=1:
        next_room=nextneighborstack.pop(-1)
        visited[next_room]=nextneighborstack
        directiontotravel=newneighbors[next_room]
        allforks.append((player.current_room.id,[directiontotravel]))
        traversal_path += directiontotravel.__str__()
        dft(next_room,visited)

    if newneighborscount==1:
        next_room=nextneighborstack.pop(-1)
        visited[next_room]=nextneighborstack
        directiontotravel=newneighbors[next_room]
        allforks[-1][1].append(directiontotravel)
        traversal_path=[*traversal_path,directiontotravel]
        dft(next_room.id,visited,traversal_path)

    return print(f'player.current_room|{player.current_room.id}|\n traversal_path| {traversal_path}|\n visited| {visited} | \n newneighbors | {newneighbors} |\n\n')
   

    if newneighborscount==0:
        if len(allforks) is None:
            return f'wheres the maze dude'
        else:
            lastfork=allforks.pop(-1)
            next_room=lastfork[0]
            if next_room not in visited:
                visited[next_room]=nextneighborstack
            walkbackwards=lastfork[1].reverse()
            breadcrumbs=[backtrack[i] for i in walkbackwards]
            traversal_path=[*traversal_path,*breadcrumbs]
            dft(next_room,visited)


dft(world.starting_room,visited={})
print (f'traversal_path{traversal_path}')

## <---------my code to find the traversal path lives above this line------>
## <--------- test config lives down there below this line------>
# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
