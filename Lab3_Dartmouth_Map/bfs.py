#Breadth first search function
#Oct. 31 2018
#Author: Sarah Korb
#Professor Cormen- CS1

from collections import *
from vertex import *
def bfs(start, end):
    q = deque()     #make an empty queue
    path = []       #make an empty list- this will hold the path
    backpointers = {}   #make a dictionary of backpointers
    backpointers[start] = None      #the starting vertex has no backpointer (nothing is before it)
    q.append(start)                 #begin the queue with the starting vertex

    while q:                        #while there is something in the queue:
        current = q.popleft()       #pop left, or check the next thing in the queue
        if current == end:          #if this object is our end vertex (aka our goal)
            while backpointers[current] != None:    #while the object in the dictionary has a backointer
                path.append(current)                #append it to the path
                current = backpointers[current]     #now the current object is its backpointer (the vertex before it)- so we can move from our end to the start
            path.append(start)                      #the while loop will not hold when we reach the start because it has no backpointer, so we append it manually here
            return path                             #return the path

        else:                                       #if we have not reached the end:
            for neighbour in current.adj_list:      #iterate through the vertex objects list of adjacent vertices
                q.append(neighbour)                 #append all of these adjacent vertices to the q
                if neighbour not in backpointers:   #if the adjacent vertex has not been visitied yet (i.e it is not in the dictionary of backpointers)
                    backpointers[neighbour] = current   #add it to the dictionary. It's backpointer is the original vertex object we were just on.











