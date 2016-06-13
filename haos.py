# fenv/bin/python

import turtle
import random


def draw_point(x, y, my_turtle):
    my_turtle.penup()
    i = 0
    while i < len(x):
        my_turtle.penup()
        my_turtle.goto(x[i], y[i])
        my_turtle.dot(2, "#2A8D9C")
        my_turtle.end_fill()
        my_turtle.pendown()
        i += 1


def serpinsky(points, my_turtle):
    x = []
    y = []
    x.insert(0, -100)
    y.insert(0, -50)
    i = 1
    while i < 2000:
        random_number = random.random()
        p1 = 1.0 / 3.0
        p2 = 2.0 / 3.0
        if random_number <= p1:
            x_a = points[0][0]
            y_a = points[0][1]
        elif p1 < random_number < p2:
            x_a = points[1][0]
            y_a = points[1][1]
        else:
            x_a = points[2][0]
            y_a = points[2][1]
        x.insert(i, (x[i-1]+x_a) / 2)
        y.insert(i, (y[i-1]+y_a) / 2)
        i += 1
    draw_point(x, y, my_turtle)


def main():
    my_turtle = turtle.Turtle()
    my_turtle.speed(0)
    my_win = turtle.Screen()
    my_points = [[-100,-50], [0,100], [100,-50]]
    serpinsky(my_points, my_turtle)
    my_win.exitonclick()

if __name__ == "__main__":
    main()
