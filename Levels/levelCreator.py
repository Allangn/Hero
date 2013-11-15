import pygame, sys
from pygame.locals import *

def main():

	# -- ask for input and introduce -- 
	print "Welcome to the Level Generator"
	print "Remember that the upper left pixel is the platform color"
	print ""
	inputstring = str(raw_input("Enter the filename of level:"))
	step = int(raw_input("What should the resolution be diveded with: "))

	# -- attributes --
	textfile = open("formatted_levels.txt", "a")

	levelmap = load_image(inputstring)

	width, height = width_height(levelmap)

	platform_color = levelmap.get_at((0,0))
	spike_color = levelmap.get_at((width - 1, 0))
	exit_color = levelmap.get_at((0, height- 1))

	print "This is the platform_color:", platform_color
	print "This is the spike_color:", spike_color
	print "This is the exit_color:", exit_color 

	# -- the empty level list --
	level_list = []

	# -- making rough map --
	mapping(levelmap, width, height, platform_color, spike_color, exit_color, level_list)

	# -- print pretty --
	formatted_level = print_pretty(level_list, step, height)

	# -- writing to file --
	textfile.write("\n")
	textfile.write("This is the layout for: ")
	textfile.write("\n")
	textfile.write(inputstring)
	textfile.write("\n")
	textfile.write("\n")
	textfile.write("The resolution is divided with: ")
	textfile.write("\n")
	textfile.write(str(step))
	textfile.write("\n")
	textfile.write("\n")
	textfile.write(str(formatted_level))
	textfile.close()

#-- to load --
def load_image(img_name):
        
	image = pygame.image.load(img_name)
	return image

#-- to get width and height --
def width_height(image):

		width, height = image.get_size()

		return width, height

# -- to make the string map --
def mapping(image, width, height, platform_color, spike_color, exit_color, level_list):

	for row in xrange(0, height):
		level_list.append([])

		for col in xrange(0, width):
			color = image.get_at((col, row))

			if color == platform_color:
				level_list[row].append("P")

			elif color == spike_color:
				level_list[row].append("N")

			#elif color = exit_color:
			#	level_list[row].append("E")
			else:
				level_list[row].append("0")

# -- to print pretty --
def print_pretty(lst, step, height):
	row = ""
	index = 0
	format_level = []

	for n in range(0,height,step):
		for l in lst[n]:
				index += 1
				if index == 1:
					row += l
				elif index == step:
					index = 0

		format_level.append(row)
		print row
		row = ""

	return format_level

main()
