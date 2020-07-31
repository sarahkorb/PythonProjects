from cs1lib import  *
from sort_cities import world_city_list

def what_city(n):
    if 1 <= n <= 50:
        return True
def get_city():
    n = int(input("Enter a number 1-50 to see what city holds that rank and its population:"))
    while not what_city(n):
        n = int(input("That number was not between 1 and 50.Enter a number 1-50 to see what city holds that rank and its population:"))
    return (n , world_city_list[n-1].name(), world_city_list[n-1].population)

print(get_city())