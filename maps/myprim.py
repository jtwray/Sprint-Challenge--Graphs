
def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):

        if len(path) == 0:
            path.append(starting_vertex)
        # base case?
        # In a search, when are we done searching?
        if starting_vertex == destination_vertex:
            return path

        visited.add(starting_vertex)

        neighbors = self.get_neighbors(starting_vertex)

        if len(neighbors) == 0:
            return None

        for neighbor in neighbors:
            if neighbor not in visited:
                new_path = path + [neighbor]
                result = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)

                if result is not None:
                    return result


    
# have all rooms\

#  from first room
"""
discovered_rooms=[]

def findNeighbors(room,discovered_rooms=[]):
    roomidx=room
    neighbors=mapped_adjacency_list[roomidx][1]
    for neighbor in neighbors:
        discovered_rooms.append(neighbor)

plan

from first room
    
    -- retrieve edges from adjacencylist using room vertice
    --loop through edges
    -- add each to the discovered_rooms arr or dict
    -- next_room= discovered_rooms[-1] or discovered_rooms[len(discovered_rooms)-1]
    findNeighbors(nextroom)
base_case
    -- next room is null


    theres this part about getting from the current room to the nextroom
        -- if thenext room is a neighbor of this room
                    the path is direct
            if getNeighbors.lenght returns None or Null:
                
            the next room is the last on the deiscoverrooms list
            do i need to do ashortest path to that room or is it stored in the 


"""


"""

visited = []
 neighborstovisit=[]

 pathsofar=[]
 pathfromlastfork=[]
 pathbacktolastfork=pathfromlastfork.reverse()


"""

"""

from first room

check for neighbors

neighbors ={}

neighbor key value = neighborid : neighbor.exits

traversal_order=[]

append current_room to traversal_order

checkVisitedforNextNeighbor()
current_room = neighbors[-1]
neightbors[-1] in visited?
    neigbors.pop()
    checkVisited(current_room)
else:
    current_room =  neighbors.pop()

    


"""

 #the entire path ['n','n','e','w','n','n','w','s','n','e','n'....]
traversal_path=[]

#directionwe just came from
backtrack={"n":"s","s":"n","e":"w","w":"e"}

#path we are currently exploring
cur_path_tracker= []

#current_room.id:current_room.get_exits()
visited={}
visited[player.current_room.id]= player.current_room.get_exits()

def get_neighbors():
    return player.current_room.get_exits()

def dft(starting_vertex,visited=set()):
    
    print(f'current_vertex:{starting_vertex}')
    print(f'player.current_room:{player.current_room}')
    if starting_vertex in visited:
        return
    
    else:
        visited.add(starting_vertex)
        traversal_path.append(starting_vertex)
        neighbors= get_neighbors()
        
        if len(neighbors)==0:
            return None
        
        for neighbor in get_neighbors():
            dft(neighbor,visited)
    
    return traversal_path