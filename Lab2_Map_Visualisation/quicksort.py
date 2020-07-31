#Program to quicksort a list
#Author: Sarah Korb
#Oct. 16th, 2018
#Professor Cormen, CS1

def partition(the_list, p, r):                                      #partition function takes parameters p and r, which is where the user chooses to start (p) and end (r) the sublist they are sorting
    pivot = the_list[r]                                             #the pivot value is given the value of the last item in the sublist

    i = p-1                                                         #moving indices i and j: j is used to move along sublist and compare the item at its index with the pivot,
    j = p                                                           # i is the index that marks the border between items less than the pivot and those more than the pivot

    while j < r:                                                    #as long as there is more than 1 item in the sublist, partition the list

            if the_list[j] <= pivot:                                #if the item is less that the pivot, increment i and then switch the item at that index with the item at index j
                i += 1
                the_list[i], the_list[j] = the_list[j], the_list[i]
            j = j+1                                                 #whether the item is less than or greater than the pivot, j is incremented

    the_list[i+1], the_list[r] = the_list[r], the_list[i + 1]       #once the whole list has been checked, switch the pivot into the approproate spot at the index one spot after index i
    return i+1                                                      #return the index of the pivot


def quicksort(the_list, p = 0, r = None):                           #quicksort function takes the list as a parameter and has a default of 0 and none for p and r

    if r is None:
        r = len(the_list) - 1                                       #set r equal to the length of the list minus 1

    if p < r:                                                       #as long as there is more than 1 item in the sublist, quicksort the list
        q = partition(the_list,p,r)                                 #partition function returns a value of the index of pivot. Therefore, the_list[q] = pivot
        quicksort(the_list,p,q-1)                                   #recursively sort the list from p to just before the pivot, and from just after the pivot to the end
        quicksort(the_list, q+1,r)
