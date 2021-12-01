import turtle
from turtle import *
import random                                           #importing random for generating random numbers and other random library functions
import math                                             #importing math for mathematical calculations
global turtle_pencolor                                        #declaring global variable pen color
global turtle_position                                         #declaring global variable position
global turtle_fillcolor                                      #declaring global variable Fill color

#function for drawing TRIANGLE (Tree leaves)

def  draw_triangle(centre_x, centre_y, width, height, pen_color, fill_color):
    #save_state()
    fillcolor(fill_color)
    turtle.begin_fill()
    x, y=(turtle.xcor(), turtle.ycor())
    x_middle=x + width/2.0
    x_bottom_left=x - height
    x_bottom_right=x + width + height
    y_top= y + height*2
    turtle.goto(x_bottom_left, y)
    turtle.goto(x_middle, y_top)
    turtle.goto(x_bottom_right, y)
    turtle.goto(x, y)
    turtle.end_fill()
    turtle.penup()
    #restore_state()

#function to save the turtle state
# Fetch the x and y co-ordinates and store them in the global variable
# Retrieve the color and fill color of current turtle and store
#them in global variable
def save_state():
    CENTER_X = turtle.xcor()
    CENTER_Y = turtle.ycor()
    turtle_pencolor = turtle.color()
    turtle_fillcolor  = turtle.fillcolor()
    pass

#function to save the turtle state
# Fetch the x and y co-ordinates and pen and fill color values from the global variables
# Setup the turtle pen and fill color and move the turtle
#to the co-ordinates in global variable saved by recent function
def restore_state():
    turtle.penup()
    turtle.goto(CENTER_X,CENTER_Y)
    turtle.color(turtle_pencolor)
    turtle.fillcolor(turtle_fillcolor)
    pass
    
#function for drawing circles  
def draw_circle(centre_x, centre_y, radius, pen_color, fill_color):
    #save_state()
    turtle.penup()
    fillcolor(fill_color)
    turtle.begin_fill()
    turtle.setposition(centre_x,centre_y)
    turtle.pendown()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()

 
def tree(x,y):
       triangles=3                               #draws 3 triangles
       h=random.randint( 15,  40)                #generates random height between 15 and 40
       w=random.randint( 10,  25)                #generates random width between 10 and 25
       colours =["#006400", "#556b2f", "#2e8b57", "#3cb371", "#32cd32"] #colors for trees
       c=random.choice(colours)                  #assiging random choice of colors to c variable
       draw_rectangle(x,y,w,h,"black","brown"),  #invokes draw rectangle function
       for i in range(triangles):                #for loop runs for 3 times  
              draw_triangle(x,y,w,h,"black",c)   #involes draw traingle fucntion
              height_increased=40/2              #assigning next height of triangle by diving 40/2
              turtle.sety(turtle.ycor()+height_increased) #sets y coordinates with clicked y coordinate and next height

#function for drawing tree trunk(vertical Rectangle)
def draw_rectangle(centre_x, centre_y, width, height, pen_color, fill_color):
    #save_state()
    turtle.penup()
    fillcolor(fill_color)
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.end_fill()
    #restore_state()
 
#function for stamping BIRD when user clicks on screen
def stamp_bird(x, y):
    #turtle.goto(x,y)
    turtle.shape('bird')
    turtle.fillcolor("purple")
    turtle.stamp()

#function for stamping TREE when user clicks on screen
def stamp_turtle(x, y):
    tree(x,y)
    
#function for calculating distance between points    
def distance(x1,y1,x2,y2):
    #d	=squareroot(x2-x1)**2 +(y2-y1)**2
    #(x1, y1)	=coordinates of the first point
    #(x2, y2)	=coordinates of the second point
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist  
    


    
