#City Class
#Author: Sarah Korb
#Oct. 16th, 2018
#Profesor Cormen, CS1

from cs1lib import *

class City:
    def __init__(self,code,name,region,population,latitude,longitude):                  #initialize all instance variables with their CORRECT formats (i.e integers, floats etc)

        self.code = str(code)
        self.name = str(name)
        self.region = str(region)
        self.population = int(population)
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        return (self.name + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude))      #define a __str__ method to print a string of a city with its population, langitude and longitude.
