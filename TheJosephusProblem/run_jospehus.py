from cs1lib import *
from army import *


def are_n_and_k_good(n, k):
    if int(n) >= 2 and int(k) in range(1, n + 1):
        return True


def get_n_and_k():
    n = int(input("Enter number of soliders at least 2"))
    k = int(input("Enter a spacing between soldiers in the range of 1 to the total number of soldiers"))
    while not are_n_and_k_good(n, k):
        n = input("That number wasn't in the right range.Enter number of soliders at least 2")
        k = input("That number wasn't in the right range.Enter a spacing between soldiers in the range of 1 to the total number of soldiers")
    (Army(n).kill_all(k))


print(get_n_and_k())




