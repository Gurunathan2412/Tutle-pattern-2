
from turtle import Turtle, Screen
import random
colour_list = [(226, 231, 236), (58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (142, 178, 203), (139, 82, 105), (208, 90, 69), (237, 225, 233), (188, 80, 120), (69, 105, 90), (133, 182, 135), (133, 133, 74), (64, 156, 92), (47, 156, 193), (183, 192, 201), (213, 177, 191), (19, 58, 92), (20, 68, 113), (113, 123, 149), (227, 174, 166), (172, 203, 183), (156, 206, 217), (69, 58, 47), (72, 64, 53), (111, 46, 59), (53, 70, 64)]

timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.penup()
a = -220
timmy.goto(-220, a)
for i in range(10):
    for n in range(10):
        timmy.color(random.choice(colour_list))
        timmy.dot(20)
        timmy.forward(50)
    a += 50
    timmy.goto(-220,a)

screen.exitonclick()
