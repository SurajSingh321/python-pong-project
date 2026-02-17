from turtle import Turtle

TOP_LIMIT = 240
BOTTOM_LIMIT = -240
STEP = 20





class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("White")
        self.shape("square")
        self.turtlesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(position)

    # def go_up(self):
    #     new_y = self.ycor()+20
    #     self.goto(self.xcor(),new_y)
    # def go_down(self):
    #     new_y = self.ycor()-20
    #     self.goto(self.xcor(),new_y)
    
    def go_up(self):
        if self.ycor() + STEP <= TOP_LIMIT:
            self.goto(self.xcor(), self.ycor() + STEP)

    def go_down(self):
        if self.ycor() - STEP >= BOTTOM_LIMIT:
            self.goto(self.xcor(), self.ycor() - STEP)
