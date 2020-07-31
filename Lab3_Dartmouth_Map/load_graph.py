#CHECKPOINT
#function to load the data and create a graph data structure and a dictionary of vertices
#Author: Sarah Korb
#Oct. 31 2018
#Professor Cormen- CS1
from vertex import *

def load_graph (file):
    vertex_dict = {}                            #create a dictionary
    in_file = open(file, "r")
    for line in in_file:                        #read through lines of file. strip and split at ";" to split line up into 3 pieces we can index into
        line = line.strip()
        line = line.split((";"))
        name = line[0]                          #the first section is the name
        coordinates = line[2].split(",")        #we split the last section again so we can index into it and get the x and y coordinates separately
        x_co = int(coordinates[0])
        y_co = int(coordinates[1])
        vertex_dict[name] = Vertex(name,x_co,y_co)  #create a vertex object with these parts as the parameters. This is done for every line- so every location in the text file is anow a reference to a vertex object

    in_file.close()                                 #close this file

    second_time = open(file, "r")                   #open the file a second time
    for line in second_time:                        #repeat what we diod before- split each line into 3 parts to index into
        line = line.strip()
        line = line.split((";"))
        name = line[0]                              #save the first section of each line to the variable 'name'
        adjacent = line[1].split(",")               #turn the second section of each line into a list by indexing into it and splitting it again by each ','

        for vertex in adjacent:                     #iterate through this list, and strip each name of whitespace
            vertex = vertex.strip()
            vertex_dict[name].append(vertex_dict[vertex])           #as every name has already been made into a reference to an object in the dictionary, use this list of strings as keys to go into the dictionary
                                                                    #then append these OBJECTS to the original vertex which we access using 'name' as the key
    second_time.close()                                             #REMEMBER: the append method was written in the vertex class and specifically appends to the object's adj_list!
                                                                    #close the file and return a reference to the dictionary
    return vertex_dict















