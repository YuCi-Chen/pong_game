from turtle import Turtle


class Paddle(Turtle):

    # TODO: Create and move a paddle
    def __init__(self, position):
        super().__init__()
        self.speed("slow")
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y_pos = self.ycor() + 20
        self.goto(self.xcor(), new_y_pos)

    def go_down(self):
        new_y_pos = self.ycor() - 20
        self.goto(self.xcor(), new_y_pos)

