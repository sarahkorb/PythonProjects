#Lab 2 CHECKPOINT
#program to write world cities with their population,langitude, longitude in a text file
#Author: Sarah Korb
#Oct. 16th, 2018
#Professor Cormen, CS1

from cs1lib import *
from city import *    #import methods from City class


in_file = open("world_cities (1).txt")       #open the text file with the information we need

world_city_list = []                            #create an empty list to hold the City objects we are going to create

for line in in_file:
    line = line.strip()                         #for every line in the world_cities text file, strip each line and split each of the elements with commas
    line = line.split(",")
    world_city = City(line[0],line[1],line[2],line[3], line[4],line[5])         #create an City object using each element in the line as a parameter for the  __init___ method of the City Class
                                                                                #obejct is created for each line because of for-loop
    world_city_list.append(world_city)                                          #as each City object is created, append it to the empty list


in_file.close()                                                                 #close the file

out_file = open("cities_out.txt", "w")                                          #open a new file to write in

for i in range(len(world_city_list)-1):                                         #iterate through the list of city objects. Index into the list at every index except for the last one
    out_file.write(world_city_list[i].__str__() +"\n")                          #use the __str___ method in the City class to write each object at each index (except for the last) into the file, starting a newline after each

out_file.write(world_city_list[-1].__str__())                                   #exit out of for loop and write the last city object into the file using the ___str___ method to avoid a blank line at the end

out_file.close()          #close the file





































