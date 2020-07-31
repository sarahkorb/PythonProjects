#Program to visualize cities on a map
#Author: Sarah Korb
#Oct. 16th, 2018
#Professor Cormen, CS1


from cs1lib import *
from sort_cities import world_city_list

img = load_image("world.png")                   #save reference retunred by load_image to be used as paramter in draw_image function
i = 0
draw = True
WINDOW_WIDTH= 720                               #Window width and height are constants that will be used as parameters of start graphics
WINDOW_HEIGHT = 360
CONVERSION_FACTOR = WINDOW_WIDTH//360           #conversion factor used to convert latitudes and longitudes so they fit in the graphics window


def main():
    global img, i, draw
    set_fill_color(1, 0, 0)                 #set fill to red


    if draw is True:
        draw_image(img,0,0)                 #only draw the background once so that it does not cover up the dots as they are drawn
        draw = False


    if i <= 50:                                                                                                             #iterate through first 50 cities in the list, using the latitudes and longitudes to get the coordinates for each dot
        world_city_list[i].longitude = ((world_city_list[i].longitude)*CONVERSION_FACTOR)+(WINDOW_WIDTH//2)                     #convert longitude by multiplying by conversion factor and adding half of the window width
        world_city_list[i].latitude = WINDOW_HEIGHT - (((world_city_list[i].latitude)*CONVERSION_FACTOR)+ WINDOW_HEIGHT//2)     #convert longitude by multiplying by conversion factor and adding half of the window height. Subtract from Window height because Y coordinates increase downwards in graphics window.
        draw_circle(world_city_list[i].longitude, world_city_list[i].latitude,3)            #draw a circle at each cities' location
        i +=1                                                                               #increment i so that every time start_graphics calls this function we plot a new city



start_graphics(main, width=720,height=360, framerate=3.0, title= "Top 50 most populous cities")                                   #framerate is slowed so we can see the dots being plotted





