#program to solve the Towers of Hanoi puzzle using recursion
#Author: Sarah Korb
#Oct. 14th, 2018
#Professor Cormen, CS1

def solve_hanoi (n, start_peg, end_peg):
    if n == 1:                                              #define the base case
        print ("Move disk 1 from peg " + str(start_peg) + " to " + str(end_peg)) #statement to be printed when base case is reached

    else:
        spare = 6 - start_peg - end_peg             #solve for the spare peg (dependss on actual parameters of  solve_hanoi function)
        solve_hanoi(n-1, start_peg, spare)          #use recursion to move discs 1 to n-1 from the starting peg to the spare peg
        print ("Move disk "+ str(n) + " from peg " + str(start_peg) + " to " + str(end_peg)) #print the 'move' statement for the largest disk. As it is freed up by the prior recursion, no recursion is needed, we simply move it from the starting peg to the end peg.
        solve_hanoi(n-1, spare, end_peg)            #use recursion to move discs 1 to n-1 from the spare peg to the end peg, thus completing the puzzle



solve_hanoi(5,1,2)                                  #call function, no print function needed because it is included in the if statement of the base case.



