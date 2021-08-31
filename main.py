import turtle
import random

darkmode = input("Darkmode? (True, False) ")
max_circle_size = int(input("Max circle size? "))
max_square_size = int(input("Max square size? "))
square_or_circle_bias = str(input("Should circles or squares be favored? (True = squares, False = circles, 'n' = None) "))

turtle.colormode(255)
turtle.speed(0.001)
turtle.hideturtle()

if darkmode == "True":
	turtle.bgcolor("black")

def draw_rect(size):
	turtle.forward(size)
	turtle.left(90)
	turtle.forward(size)
	turtle.left(90)
	turtle.forward(size)
	turtle.left(90)
	turtle.forward(size)

while True:
	if random.randint(0,1): # To move left or right?
		turtle.right(random.randint(0, 150))
		turtle.forward(random.randint(0, 10))
	else:
		turtle.left(random.randint(0, 150))
		turtle.forward(random.randint(0, 10))

	if square_or_circle_bias == "True": # Which one should be rendered more
		if random.randint(0, 10) == 5: # Drawing circles and squares
			if square_or_circle_bias == "True": # If squares are biased
				turtle.circle(random.randint(1, max_circle_size))
			elif square_or_circle_bias == "False": # If circles are biased
				draw_rect(random.randint(1, max_square_size))
		else:
			if square_or_circle_bias == "True": # If squares are biased
				draw_rect(random.randint(1, max_square_size))
			elif square_or_circle_bias == "False": # If circles are biased
				turtle.circle(random.randint(1, max_square_size))

	elif square_or_circle_bias == "n": # If there is no bias
		if random.randint(0, 1):
			turtle.circle(random.randint(1, max_circle_size))
		else:
			draw_rect(random.randint(1, max_square_size))

	if darkmode == "True": # Coloring the lines depending on light mode or darkmode
		darkness = random.randint(0, 255)
		turtle.pencolor(darkness,darkness,darkness)
	else:
		turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
