#Writing a Test harness to test Counter class
#Author: Sarah Korb
#Professor Thomas Cormen,CS1
#Oct.7th, 2018

from counter import *  #import methods from Counter class file

#testing the counter with limit of 60, initial value of 0 and a minimum of 1 digit
#test counter methods using 3 consecutive method calls to see if the correct sequence of numbers is appearing, in this case 59,58,57

my_clock = Counter(60)      #create an object

my_clock.get_value()        #returns counter value
my_clock.tick()             #counter decreases by one/or resets
print(str(my_clock))        #print the string of the counter

my_clock.get_value()
my_clock.tick()
print(str(my_clock))

my_clock.get_value()
my_clock.tick()
print(str(my_clock))

#testing the counter with a limit of 60 and an initial value of 2.
# Check to see if sequence begins at 2 and then resets after it goes negative (i.e the console should print 1,0,59)
my_new_clock = Counter (60,2)

my_new_clock.get_value()
my_new_clock.tick()
print(str(my_new_clock))

my_new_clock.get_value()
my_new_clock.tick()
print(str(my_new_clock))

my_new_clock.get_value()
my_new_clock.tick()
print(str(my_new_clock))


#testing the counter with a limit of 60, an inital value 1 and a minimum digit value of 5.
# Check to see if the console prints correct numbers with correct amount of zeros on the left side. The counter should also reset in this sequence
my_final_clock = Counter(60,1,5)

my_final_clock.get_value()
my_final_clock.tick()
print(str(my_final_clock))

my_final_clock.get_value()
my_final_clock.tick()
print(str(my_final_clock))

my_final_clock.get_value()
my_final_clock.tick()
print(str(my_final_clock))


my_error_clock = Counter (60, -1, 1) #testing counter to see if error message appears when initial is less than 0`

my_error_clock.get_value()
my_error_clock.tick()
print(str(my_error_clock))





