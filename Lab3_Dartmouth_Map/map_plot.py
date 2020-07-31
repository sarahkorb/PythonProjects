#Function to draw the map and use the mouse callback functions
#Author: Sarah Korb
#Oct. 31 2018
#Professor Cormen- CS1


from cs1lib import *
from vertex import *
from load_graph import *
from bfs import *


start_vertex = None                 #start vertex begins as none
goal_vertex = None                   #goal vertex begins as none
start_vertex_chosen = False         #a start vertex has not been chosen yet
img = load_image("dartmouth_map.png")       #save reference returned by load_image in variable img
dictionary = load_graph("dartmouth_graph.txt")      #load_graph returns a reference to a dictionary of all the vertices and thier adjacent verticies. Save this in the variable dictionary
WIDTH = 1021        #constants
HEIGHT = 811


def mouse_click(mx, my):                    #mouse press callback function
    global click, x, y, start_vertex, start_vertex_chosen
    x = mx
    y = my
    for vertex in dictionary:                               #if the mouse is clicked, check that the click happened over a vertex. Do this by iterating through the dictionary of verticea and using the bounding box method
            if dictionary[vertex].in_bounding_box(x,y):
                start_vertex_chosen = True                  #if the click happened over a vertex, a starting vertex has been chosen.
                start_vertex = dictionary[vertex]           #the start vertex gets the value of the object in the dictionary stored under this key

def mouse_hover(mx, my):                                #mouse move callback function
    global goal, x, y, goal_vertex
    x = mx
    y = my
    goal_vertex = choose_goal()                         #goal_vertex gets the value returned by the choose_goal function


def draw_verticies():                                   #draws all the vertices and edges on the map
    for vertex in dictionary:
        dictionary[vertex].draw_vertex(0,0,1)
        dictionary[vertex].draw_all_edges(0,0,1)


def choose_goal():
    global start_vertex_chosen
    if start_vertex_chosen:                             #if a start vertex has been chosen...
        for vertex in dictionary:                       #iterate through the dictionary and check that the mouse is hovering over a vertex (use the bounding_box method)
            if dictionary[vertex].in_bounding_box(x, y):
                goal = dictionary[vertex]               #if it is hovering over a vertex, save the reference to the object in the dicitonary under this key in the variable goal
                return goal                             #return this reference
        return None                                     #otherwise, return none- a goal vertex has not been chosen

def draw_background():
    draw_image(img, 0, 0)


def main():

    global start_vertex_chosen, start_vertex, goal_vertex
    draw_background()
    draw_verticies()
    if start_vertex != None:                                #if there is a starting vertex...
        start_vertex.draw_vertex(1,0,0)                     #draw this vertex in red and its name
        start_vertex.draw_name()
    if goal_vertex != None:                                 #if there is a goal vertex...
        goal_vertex.draw_vertex(1,0,0)
        goal_vertex.draw_name()                             #draw this vertex in red and its name
        path = bfs(start_vertex, goal_vertex)               #save the reference to the list returned by the bfs function
        for i in range(len(path)-1):                        #iterate through this list of vertex objects. Draw each object and an edge between the object and the object after it.
            path[i].draw_edge(path[i + 1], 1, 0, 0)
            path[i].draw_vertex(1,0,0)


start_graphics(main, mouse_press= mouse_click, mouse_move= mouse_hover, width= WIDTH, height= HEIGHT)


