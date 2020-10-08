## currentroom = 0
# currentroom_neighbors= currentroom.getNeighbors()
#
# 
# 
# 
# find roomnumber for neighbors of currentroom
# store neighbors in set discovered_neighbors## 
#def getNeighbors(currentroom):
#   exitdirections=currentroom.get_exits()
# if exitdirections == None:
#   return
# for exit in exitdirections:
#   room_number=currentroom.get_room_in_direction(exit)
#   if room_number in discovered_rooms:#
#   discovered_rooms[room_number]=[currentroom,exit]
# #
#   #
##


#
# 
# #
#getneighbors
# neighbors comes form this
# {
#   0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
#   1: [(3, 6), {'s': 0, 'n': 2}],
#   2: [(3, 7), {'s': 1}],
#   3: [(4, 5), {'w': 0, 'e': 4}],
#   4: [(5, 5), {'w': 3}],
#   5: [(3, 4), {'n': 0, 's': 6}],
#   6: [(3, 3), {'n': 5}],
#   7: [(2, 5), {'w': 8, 'e': 0}],
#   8: [(1, 5), {'e': 7}]
# }
# #
#
# path from fork
# each time a neighbor is set to currentroom#
# 
# traversalpath
# add to traversalpath eachtime a currentroomchanges


# visited
# add to visited when all neighbors are visited
# 
# #

# Python implementation to find the  
# shortest path in the graph using  
# dictionaries  
  
# Function to find the shortest 
# path between two nodes of a graph 
def BFS_SP(graph, start, goal): 
    explored = [] 
      
    # Queue for traversing the  
    # graph in the BFS 
    queue = [[start]] 
      
    # If the desired node is  
    # reached 
    if start == goal: 
        print("Same Node") 
        return
      
    # Loop to traverse the graph  
    # with the help of the queue 
    while queue: 
        path = queue.pop(0) 
        node = path[-1] 
          
        # Codition to check if the 
        # current node is not visited 
        if node not in explored: 
            neighbours = graph[node] 
              
            # Loop to iterate over the  
            # neighbours of the node 
            for neighbour in neighbours: 
                new_path = list(path) 
                new_path.append(neighbour) 
                queue.append(new_path) 
                  
                # Condition to check if the  
                # neighbour node is the goal 
                if neighbour == goal: 
                    print("Shortest path = ", *new_path) 
                    return
            explored.append(node) 

traversal_path=[]

def getneighbors():
    return player.current_room.get_exits()

def get_room_in_direction(exit):
    return player.current_room.get_room_in_direction(exit)

def dft(startingdir,visited=set(),unvisitedneighbors=[]):
    if get_room_in_direction(startingdir) in visited:
        return
    else:
        visited.add(get_room_in_direction(startingdir))
        traversal_path.append(startingdir)
        neighbors=getneighbors()
        for neighbor in neighbors:
            if get_room_in_direction(neighbor) not in visited:
                unvisitedneighbors.append(get_room_in_direction(neighbor))
                dft(unvisitedneighbors[-1],visited,unvisitedneighbors)
            if get_room_in_direction(neighbor) in visited:
                traversal_path.extend(bft(map,player.current_room,unvisitedneighbors[-1]))



