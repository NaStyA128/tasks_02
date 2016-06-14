import turtle
import re
import random
from collections import Counter


class Diagrams:

    COLORS = ["#CED23A", "#002F55", "#44944A",
              "#6E5160", "#CD7F32", "#990066",
              "#6A5ACD", "#1CAC78", "#FF0033",
              "#7A7666", "#806B2A", "#FF8C69"]

    input_text = ""
    legend_start_point_y = 200

    def __init__(self, text, my_turtle):
        self.input_text = text
        self.__sector__(my_turtle)

    def __sector__(self, my_turtle):
        words = re.sub('\W', ' ', self.input_text).split()
        count_word = Counter(words)
        total_words = len(words)

        for c in count_word:
            color = random.choice(self.COLORS)
            my_turtle.fillcolor(color)
            my_turtle.pencolor("white")
            my_turtle.pensize(3)
            angle = 360.0*count_word[c] / total_words
            my_turtle.pendown()
            my_turtle.begin_fill()
            my_turtle.forward(140)
            my_turtle.left(90)
            my_turtle.circle(140, angle)
            my_turtle.left(90)
            my_turtle.forward(140)
            my_turtle.left(180)
            my_turtle.end_fill()
            self.__legend__(c, count_word[c], color, my_turtle)
        my_turtle.hideturtle()

    def __legend__(self, word, quantity, color, my_turtle):
        my_turtle.penup()
        self.legend_start_point_y -= 20
        my_turtle.goto(200, self.legend_start_point_y)
        my_turtle.pencolor(color)
        my_turtle.pensize(1)
        my_turtle.pendown()
        my_turtle.dot(15)
        my_turtle.penup()
        my_turtle.goto(220, self.legend_start_point_y - 5)
        my_turtle.pendown()
        my_turtle.write(word + ' - (' + repr(quantity) + ') time (-s)')
        my_turtle.penup()
        my_turtle.setpos(0, 0)


def main():
    turt = turtle.Turtle()
    turt.speed(10)
    Diagrams("My name is Nastya. My cat is cool. It is funny.", turt)
    turtle.done()

if __name__ == "__main__":
    main()
