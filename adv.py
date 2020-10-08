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
visited_rooms={}
allforks=[]
currentroom=0
nextneighborstack=[]


#direction we just came from
backtrack={"n":"s","s":"n","e":"w","w":"e"}

def get_neighbors():
    return player.current_room.get_exits()

def dft(starting_vertex,visited=set()):
    player.current_room=starting_vertex
    newneighbors=get_neighbors()
    newneighborscount=0
    for neighbor in newneighbors:
        if neighbor not in visited:
            nextneighborstack.append(player.current_room.get_room_in_direction(neighbor))
            newneighborscount+=1
    
    if newneighborscount==0:
        if len(allforks) is None:
            return f'wheres the maze dude'
        else:
            lastfork=allforks.pop(-1)
            walkbackwards=list(reversed(lastfork))
            breadcrumbs=[backtrack[i] for i in walkbackwards]
            traversal_path=[*traversal_path,*breadcrumbs]
            dft()



    current_path=[]
    if starting_vertex in visited:
        return
    
    else:
        visited[starting_vertex]= player.current_room.get_exits()
        
        neighbors= get_neighbors()

        next_room = player.current_room.get_room_in_direction(neighbor)
        # traversal_path.append(starting_vertex)
        
        if len(neighbors)==0:
            return None
        
 
    for neighbor in get_neighbors():

        if player.current_room.get_room_in_direction(neighbor) in visited:
            return 
            traversal_path.append(neighbor)
            dft(player.current_room.get_room_in_direction(neighbor),visited)
    
    return traversal_path
    



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
