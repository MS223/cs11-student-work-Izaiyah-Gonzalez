class color(object):
    """Represents a color"""

my_color_1 = color()
my_color_1.red = 139
my_color_1.green = 0
my_color_1.blue = 0

my_color_2 = color()
my_color_2.red = 124
my_color_2.green = 252
my_color_2.blue = 0

my_color_3 = color()
my_color_3.red = 0
my_color_3.green = 255
my_color_3.blue = 255

my_colors = [my_color_1, my_color_2, my_color_3]


def add_color(my_color_1, my_color_2):
    red_sum = my_color_1.red + my_color_2.red
    green_sum = my_color_1.green + my_color_2.green
    blue_sum = my_color_1.blue + my_color_2.blue
add_color()
    print red_sum / 2, green_sum / 2, blue_sum / 2
