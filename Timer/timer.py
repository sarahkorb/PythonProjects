#Program to make a timer for 24 hours
#Author: Sarah Korb, worked with Jennifer Quian and Jay Kang
#Professor Cormen, CS1
#Oct. 7th, 2018

#import methods from counter to use in Timer class
from counter import *

class Timer:

    #initialize instance variables
    def __init__(self, hours, minutes, seconds):
        #the instance variables will be given by references from three Counter constructors
        self.hours = Counter(24,hours,2)
        self.minutes = Counter(60, minutes, 2)
        self.seconds = Counter(60, seconds, 2)

    #method will return a string of the values on the timer in the format hours:minutes:seconds
    def __str__(self):

        return (str(self.hours) + ": " + str(self.minutes) + ": " + str(self.seconds))


    #method will decrease the values on the timer by 1 starting with seconds.
    #when the seconds hit 0, the minutes will begin to decrease
    #when the minutes hit 0 the hour value will decrease
    def tick(self):

        if self.seconds.tick():
            if self.minutes.tick():
                self.hours.tick()

    #returns a boolean value. Will be True if the hours,minutes and seconds on the timer are all zero
    def is_zero(self):

        return self.hours.get_value()== 0 and self.minutes.get_value() == 0 and self.seconds.get_value() == 0













