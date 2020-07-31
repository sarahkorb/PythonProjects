from cs1lib import *
from sort_cities import world_city_list

img = load_image("world.png")                            #save reference retunred by load_image to be used as paramter in draw_image function
i = 0
draw = True
WINDOW_WIDTH= 720                                         #Window width and height are constants that will be used as parameters of start graphics
WINDOW_HEIGHT = 360
CONVERSION_FACTOR = WINDOW_WIDTH//360                     #conversion factor used to convert latitudes and longitudes so they fit in the graphics window


click = False                                               #mouse hasn't been clicked yet

def mouse_click(mx,my):                                     #when mouse is clicked, record the x and y coordinates and click turns true
    global click, x, y
    x = mx
    y = my
    click = True


def release(mx, my):                                        #when mouse is released, record the x and y coordinates and click turns false
    global click, x, y
    x = mx
    y = my
    click = False

def show_population():
    global i
    if click:                                                   #if the mouse is clicked within 5 units of a city coordinate, show the population of that city and its rank
        for i in range(len(world_city_list)):
            if (world_city_list[i].longitude - 5 <= x <= world_city_list[i].longitude + 5) and (world_city_list[i].latitude - 5 <= y <= world_city_list[i].latitude + 5):
                cover_up()
                write_city()

def draw_instructions():
    set_font_size(10)
    draw_text("Click on a city to see its population",5,250)
    draw_text("KEY :", 5, 270)
    set_stroke_color(1,0,0)                              #The top city is shown in red
    draw_text("Top City", 5, 280)
    set_stroke_color(1, 1, 0)                               #The top 5 are shown in yellow
    draw_text("Top 5 Cities", 5, 290)
    set_stroke_color(0,0,1)                                 #The remaining cities are shown in blue
    draw_text("Top 50 Cities", 5, 300)


def cover_up():                                     #draw a blank rectangle every time a population is show so that the words do not overlap eachother
    disable_stroke()
    set_fill_color(1, 1, 1)
    draw_rectangle(295, 290, 170, 20)

def write_city():                                   #function to write the population/rank/name of the city of the bottom of the window
    set_font_size(10)
    enable_stroke()
    set_stroke_color(0, 0, 0)
    set_font_bold()
    draw_text(str(i + 1) + ". " + world_city_list[i].name + ":" + str(world_city_list[i].population), 300, 300)


def draw_50():                  #draw the 50 dots with the ranks next to them and the respecitve colors depending on thier ranks. Also draw the name/rank/population at the bottom of the window as every dot is drawn.
    global i
    if i == 0:
        world_city_list[i].longitude = ((world_city_list[i].longitude) * CONVERSION_FACTOR) + (WINDOW_WIDTH // 2)
        world_city_list[i].latitude = WINDOW_HEIGHT - (((world_city_list[i].latitude) * CONVERSION_FACTOR) + WINDOW_HEIGHT // 2)
        set_stroke_color(0, 0, 0)
        set_fill_color(1, 0, 0)
        draw_circle(world_city_list[i].longitude, world_city_list[i].latitude, 5)
        set_font_size(10)
        draw_text(str(i + 1), world_city_list[i].longitude + 2, world_city_list[i].latitude - 2)
        cover_up()
        write_city()
        i += 1

    elif i <= 5:
        world_city_list[i].longitude = ((world_city_list[i].longitude) * CONVERSION_FACTOR) + (WINDOW_WIDTH // 2)
        world_city_list[i].latitude = WINDOW_HEIGHT - (((world_city_list[i].latitude) * CONVERSION_FACTOR) + WINDOW_HEIGHT // 2)
        set_stroke_color(0,0,0)
        set_fill_color(1, 1, 0)
        draw_circle(world_city_list[i].longitude, world_city_list[i].latitude, 5)
        set_font_size(10)
        draw_text(str(i + 1), world_city_list[i].longitude + 2, world_city_list[i].latitude - 2)
        cover_up()
        write_city()
        i += 1

    elif 5 < i < 50:
        world_city_list[i].longitude = ((world_city_list[i].longitude) * CONVERSION_FACTOR) + (WINDOW_WIDTH // 2)
        world_city_list[i].latitude = WINDOW_HEIGHT - (((world_city_list[i].latitude) * CONVERSION_FACTOR) + WINDOW_HEIGHT // 2)
        set_stroke_color(0, 0, 0)
        set_fill_color(0, 0, 1)
        draw_circle(world_city_list[i].longitude, world_city_list[i].latitude, 5)
        set_font_size(10)
        draw_text(str(i + 1), world_city_list[i].longitude + 2, world_city_list[i].latitude - 2)
        cover_up()
        write_city()
        i += 1


def set_background():
    global img, draw

    if draw is True:                 #only draw the background once so that it does not cover up the dots as they are drawn
        draw_image(img,0,0)
        draw_instructions()           #only draw the instructional text/key one time
        draw = False


def main():                         #main function to be given to start graphics
    set_background()
    draw_50()
    show_population()



start_graphics(main, width=720,height=360, framerate=3.0, mouse_press= mouse_click, mouse_release= release, title= "Top 50 most populous cities")

