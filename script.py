# fenv/bin/python

import math
import turtle

my_turtle = turtle.Turtle()
my_turtle.pencolor("#646B63")
my_turtle.speed(10)


def first_triangle(count_div, side_t, dot):
    h = (math.sqrt(3)/2) * side_t
    dot[0] = dot[0] + side_t/2
    dot[1] = dot[1] - h/2

    my_turtle.fillcolor("#98FF98")
    my_turtle.penup()
    my_turtle.goto(dot)
    my_turtle.pendown()
    i = 1
    my_turtle.begin_fill()
    while i <= 3:
        my_turtle.left(120)
        my_turtle.forward(side_t)
        i = i + 1
    my_turtle.end_fill()
    my_turtle.penup()
    little_triangles(count_div, side_t/2, dot)


def little_triangles(count_div, side_t, dot):
    count_div = count_div - 1
    if count_div < 1 :
        return
    my_turtle.goto(dot)
    my_turtle.pendown()
    my_turtle.left(120)
    my_turtle.forward(side_t)
    my_turtle.fillcolor("#FADADD")
    i = 0
    my_turtle.begin_fill()
    my_turtle.left(60)
    start_dots = {}
    while i < 3:
        my_turtle.forward(side_t)
        my_turtle.left(120)
        start_dots[i] = my_turtle.pos()
        i = i + 1
    my_turtle.end_fill()
    my_turtle.left(180)
    my_turtle.penup()
    little_triangles(count_div, side_t/2, dot)
    little_triangles(count_div, side_t/2, start_dots[1])
    little_triangles(count_div, side_t/2, start_dots[2])


def main():
    start_position = [0, 0]
    first_triangle(4, 200, start_position)
    turtle.done()

if __name__ == "__main__" :
    main()