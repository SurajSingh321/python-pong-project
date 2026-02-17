from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10
        self.move_spped = 0.1
    
    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)

    # bounce ball in y direction
    def bounce_y(self):
        self.y_move*=-1
        
    # bounce ball in x direction
    def bounce_x(self):
        self.x_move*=-1
        self.move_spped*=0.9

    #RESET BALL
    def reset_position(self):
        self.goto(0,0)
        self.move_spped = 0.1
        self.bounce_x()