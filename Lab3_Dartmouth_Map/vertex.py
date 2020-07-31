from cs1lib import *
#CHECKPOINT
#Class to create vertex objects
#Author: Sarah Korb
#Oct. 31 2018
#Professor Cormen; CS1
RADIUS = 7
STROKE_WIDTH = 4
class Vertex:
    def __init__(self, name, x, y,):            #initialise the instance variables- each object should have a (x,y) coordinate and an empty list of adjacent vertices
        self.name = name
        self.x = x
        self.y =y
        self.adj_list = []

    def append(self, vertex):                   #method to append other adjacent vertex objects to the list of adjacent vertices
        self.adj_list.append(vertex)

    def make_string(self):                      #method to make the objects in the adj_list into strings so they can be printed
        string = ''                             #make an empty string, iterate throguh the list and concatonate this string with the STRING of the name of each vertex object (and a comma)
        for place in self.adj_list:
            string = string + str(place.name) + ", "
        string = string[0:-2]                   #splice this string  to avoid getting an extra space and comma after the last name
        return string                           #return the string

    def __str__(self):
        return (str(self.name) + ";" + "Location:" + str(self.x) +  "," + str(self.y) + ";" + "Adjacent vertices: " + self.make_string() )  #method to string a vertex object


    def draw_vertex(self, r, g, b):     #method to draw vertex
        set_fill_color(r, g, b)
        set_stroke_color(r, g, b)
        draw_circle(self.x, self.y, RADIUS)


    def draw_edge(self, other, r, g, b):            #method to draw edge between two vertices takes the other vertex object as a parameter
        set_stroke_color(r,g,b)
        set_stroke_width(STROKE_WIDTH)
        draw_line(self.x, self.y, other.x, other.y)

    def draw_all_edges(self,r,g,b):                 # method to draw all edges between the vertices iterates through adjacent list and draws a line between the vertex object and every vertex in that list
        set_stroke_color(r,g,b)
        for vertex in self.adj_list:
            set_stroke_width(STROKE_WIDTH)
            draw_line(self.x,self.y, vertex.x, vertex.y)

    def in_bounding_box(self, x, y):                    #method to see whether a mouse click was within the radius of the vertex. returns a boolean
        return self.x - RADIUS <= x <= self.x + RADIUS and self.y - RADIUS <= y <= self.y + RADIUS

    def draw_name(self):                                #EXTRA CREDIT: method to draw the name of the location
        draw_text(str(self.name), self.x - RADIUS, self.y - RADIUS - RADIUS)













