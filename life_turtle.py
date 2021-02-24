from turtle import Turtle

START_X_CORR = -350
START_Y_CORR = 200
STEPS = 8
SIZE = 0.3

class Life:

    def __init__(self, years):
        self.start_x = START_X_CORR
        self.start_y = START_Y_CORR
        self.steps = STEPS
        self.size = SIZE
        self.weeks = round(years * 52.1786)
        self.age = 0
        self.week_list = []

        self.create_weeks()

    def create_weeks(self):

        x_cor = self.start_x
        y_cor = self.start_y

        for week in range(self.weeks):
            new_week = Turtle()
            new_week.hideturtle()
            new_week.speed("fastest")
            new_week.shapesize(self.size)
            new_week.shape("square")
            new_week.fillcolor("white")
            new_week.penup()

            y_cor -= self.steps

            if week % 50 == 0:
                y_cor = self.start_y
                x_cor += self.steps
            new_week.goto(x_cor, y_cor)
            new_week.showturtle()

            self.week_list.append(new_week)


    def fill_weeks(self, age):
        pass