#Creating a counter class to count down to 0 from a number
#Author: Sarah Korb, worked with Jennifer Qian
#Oct. 7th. 2018
#Professor Cormen, CS1


class Counter:
    #initialising the instance variables
    def __init__(self,limit, initial = 0, min_digits = 1):
        self.limit = limit                                      #the maximum value, or the value we are counting down from
        self.initial = initial                                  #the value we begin counting down from
        self.min_digits = min_digits                            #the minimum amount of digits to be displayed in the counter string
        if 0 <= initial <= limit - 1:
            self.initial = initial
        else:
            print ("Error")                                     #error message appears when initial is less than 0
            self.initial = limit - 1



    #method will return the value of the counter if called
    def get_value (self):
        return int(self.initial)

    #method will return the string og the counter with the apprioriate amount of zeros in front of it
    #the number of zeros is dependant on the value passed to the min_digits parameter
    def __str__(self):
        length = len(str(self.initial))
    # the number of zeros necessary for a particular string is the difference between the minimum digits required and the length of that string
        return (str("0" * (self.min_digits - length)) + str(self.initial))


    #method will decrease the counter value by one if called
    def tick(self):
        if self.initial > 0:
            self.initial -= 1
        else:
            self.initial = self.limit -1            #when value reaches 0 and would be decreased to -1, the counter resets to be the value of (limit - 1). Therefore, the counter never displays negative numbers
        return self.initial == self.limit -1        #will return the boolean value of whether the counter reset







