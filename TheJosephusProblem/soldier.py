#Define a soldier class
#Author: Sarah Korb
#October 29th, 2018
#Professor Cormen
class Soldier:

    def __init__(self, number): #initialize the instance variables
        self.number = number   #number of soldier object
        self.next = None      #it doesn't reference any other objects yet
        self.prev = None

    def kill(self, prefix, suffix = None):  #method to kill a soldier
        self.prev.next = self.next  #make the 'next' of the  previous object reference the object after the "dead" soldier
        self.next.prev = self.prev  #make the 'previous' of the next object reference the object before the "dead" soldier

        if suffix ==  None:
            print (prefix + str(self.number))
        else:
            print (prefix + str(self.number) + suffix)




