#Writing a Test harness to test Timer class
#Author: Sarah Korb
#Professor Thomas Cormen,CS1
#Oct.7th, 2018


from timer import * #import all methods from Timer class

my_timer = Timer (1,30,0)       #create an object

while not my_timer.is_zero():   #create a while loop that will print the values of the timer from its actual parameter values to when the timer reads 00:00:00
    my_timer.tick()
    print(str(my_timer))
