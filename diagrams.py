# fenv/bin/python

import turtle
import re
import random
from collections import Counter

COLORS = ["#CED23A", "#002F55", "#44944A", "#6E5160", "#CD7F32", "#990066", "#6A5ACD"]

my_turtle = turtle.Turtle()
my_turtle.pencolor("#646B63")
my_turtle.speed(10)
legend_turtle = turtle.Turtle()
legend_turtle.speed(10)


def sector_diagram(str):
    words = re.sub('\W', ' ', str).split()
    count_word = Counter(words)
    count_words = 0
    for i in words:
        count_words += 1
    my_turtle.left(90)
    my_turtle.pendown()
    legend_turtle.hideturtle()
    lt_y = 200
    for c in count_word:
        color = random.choice(COLORS)
        my_turtle.fillcolor(color)
        angle = 360 * count_word[c] / count_words
        my_turtle.begin_fill()
        my_turtle.forward(140)
        my_turtle.left(90)
        my_turtle.circle(140, angle)
        my_turtle.left(90)
        my_turtle.forward(140)
        my_turtle.left(180)
        my_turtle.end_fill()
        legend_turtle.showturtle()
        legend_turtle.penup()
        lt_y -= 15
        legend_turtle.goto(200, lt_y)
        legend_turtle.pendown()
        legend_turtle.fillcolor(color)
        legend_turtle.pencolor(color)
        legend_turtle.begin_fill()
        legend_turtle.circle(5)
        legend_turtle.end_fill()
        legend_turtle.penup()
        legend_turtle.goto(220, lt_y)
        legend_turtle.pendown()
        legend_turtle.write(c + ' - (' + repr(count_word[c]) + ') time (-s)')
        legend_turtle.hideturtle()
    my_turtle.hideturtle()


def rays_diagram(str):
    words = re.sub('\W', ' ', str).split()
    count_word = Counter(words)
    type_words, count_words = 0, 0
    for i in count_word:
        type_words += 1
    for i in words:
        count_words += 1
    angle = 360 / type_words
    # my_turtle.left(90)
    for c in count_word:
        j = 1
        my_turtle.pendown()
        my_turtle.pencolor(random.choice(COLORS))
        while j <= count_word[c]:
            my_turtle.forward(50)
            my_turtle.circle(2)
            j += 1
        my_turtle.penup()
        position = my_turtle.pos()
        print position
        if position[1] > 5.00:
            my_turtle.goto(my_turtle.xcor(), my_turtle.ycor() + 10)
        elif -5.00 < position[1] < 5.00:
            if position[0] < -5.00:
                my_turtle.goto(my_turtle.xcor() - 50, my_turtle.ycor())
            elif position[0] > 5.00:
                my_turtle.goto(my_turtle.xcor() + 20, my_turtle.ycor())
        else:
            my_turtle.goto(my_turtle.xcor(), my_turtle.ycor() - 20)
        my_turtle.pendown()
        my_turtle.write(c)
        my_turtle.penup()
        my_turtle.goto(0, 0)
        my_turtle.left(angle)
    my_turtle.hideturtle()


def main(str, method):
    if method == 'sector':
        sector_diagram(str)
    elif method == 'rays':
        rays_diagram(str)
    else:
        sector_diagram(str)

if __name__ == "__main__":
    str = 'My name - Nastya, name. LightIT. text text'
    main(str, 'sector')
    # main(str, 'rays')
    turtle.done()
