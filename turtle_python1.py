import turtle as t
import random
tim = t.Turtle()
game_over = False
num_sides = 5
tim.speed(2000)
colors = ["orange", "dark orange", "chocolate", "gold", "navajo white", "orange red"]

while not game_over:

    for _ in range(num_sides):
        tim.color(random.choice(colors))
        angle = 360 / num_sides
        tim.forward(25)
        tim.left(angle)

    num_sides += 1