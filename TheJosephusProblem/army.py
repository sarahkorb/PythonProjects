#Define a army class
#Author: Sarah Korb
#October 29th, 2018
#Professor Cormen
from soldier import *
class Army:
    def __init__(self, total):                  #initialize instance variables. 'total' parameter is the total number of soldiers in an army object
        self.alive = int(total)
        self.victim = Soldier(1)                #make a victim- create the first soldier object
        self.victim.next = self.victim          #make it reference it self
        self.victim.prev = self.victim

        for i in range(2, total + 1):           #for-loop creates soldier obects in the army
            new = Soldier(i)                    #assign reference to a soldier object to variable 'new'
            new.prev = self.victim              #its previous references the original victim (soldier 1 created in the __init___ method)
            new.next = self.victim.next         #its next references the next of the original victim
            self.victim.next.prev = new         #the next of the victim's previous, which was referencing the victim, now references the new object
            self.victim.next = new              #the victim's next now references the new object- a circularly linked list is created
            self.victim = new                   #the new object now becomes the victim, and the process repeats to continue creating a circularly linked list with all the soldiers in the army


    def advance(self, k):                       #advance function moves forward a given interval in the list of soldiers
        for i in range(k):
            self.victim = self.victim.next      #do this by making the victim the next thing in the list for k iterations


    def kill_all(self,k):                       #method to begin killing soldiers
        while self.alive > 1:                   #while there is at least 2 soldiers in the army....
            self.advance(k)                     #advance k spaces in the list
            save = self.victim.prev             #save a reference to the previous soldier to be used to continue the killing process once the soldier in front of it is killed
            self.victim.kill("Soldier ", " kicks the bucket")        #kill the soldier
            self.victim = save                                      #the new victim is the 'saved' previous soldier. We continue the 'advance and kill' process from here.
            self.alive -= 1                                         #the live count decreases by 1

        self.victim.kill("The last remaining soldier is ")          #once there is 1 soldier left, we print this statement.

#use while loops make sure user inputs are in the right range

n = int(input("Enter number of soliders at least 2: "))

while n < 2: #forces user to input a correct value in order to exit while loop
    n = int(input("That number wasn't in the right range. Enter number of soliders at least 2: "))

s = int(input("Enter a spacing between soldiers in the range of 1 to the total number of soldiers: "))

while s < 1 or s > n:
    s = int(input("That number wasn't in the right range. Enter a spacing between soldiers in the range of 1 to the total number of soldiers: "))

#create an army object with the user's input value, and then call the kill_all method using the user's spacing value
army1= Army(n)
army1.kill_all(s)
















