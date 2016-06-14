import turtle
import random


class Triangles:

    start_points, array_points = [], []

    def __init__(self, method, points, my_turtle):
        self.start_points = points
        if method == 'haos':
            self.__draw_hm__(my_turtle)

    def __draw_hm__(self, my_turtle):
        self.array_points.append(self.start_points[0])
        i = 1
        while i < 3000:
            random_number = random.random()
            if random_number < 0.3333:
                active_point = self.start_points[0]
            elif 0.3333 < random_number < 0.6666:
                active_point = self.start_points[1]
            else:
                active_point = self.start_points[2]
            new_point = ((self.array_points[i - 1][0]+active_point[0]) / 2,
                         (self.array_points[i - 1][1]+active_point[1]) / 2)
            self.array_points.append(new_point)
            i += 1
        self.__draw_points__(self.array_points, my_turtle)

    def __draw_points__(self, points, my_turtle):
        for i in points:
            my_turtle.penup()
            my_turtle.setpos(i)
            my_turtle.pendown()
            my_turtle.dot(1, '#9966CC')
        my_turtle.hideturtle()


def main():
    turt = turtle.Turtle()
    turt.speed(0)
    points = [(-100, -50), (0, 100), (100, -50)]
    Triangles('haos', points, turt)
    turtle.done()

if __name__ == "__main__":
    main()
