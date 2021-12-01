import turtle
from utilities import *                   #importing utilities module and all its functions
from turtle import *                      #importing turtle graphics llbrary and all its functions
import random                             #importing random for generating random numbers and other random library functions

screen = turtle.Screen()                  #assigning turtle screen to screen variable
turtle.setup(700, 700)                    #setting up the screen

#function for writing text on screen
#writes given text at the given goto coordinates
def text():
       turtle.goto(20, 310)
       turtle.write("Tree")
       turtle.goto(120, 310)
       turtle.write("Bird, Click left or right button to tilt")

#function for tree selection
#draws circle according to given radius and coordinates

def turtle_selector():
       draw_circle(0,310,10,"green","green")

#function for bird selection
#draws circle according to given radius and coordinates
def bird_selector():
       draw_circle(100,310,10,"green","")


#function for drawing bounday
#draws boundary based on goto coordinates
def boundary():
       turtle.penup()
       turtle.goto(-300,-300)
       turtle.pendown()
       turtle.pensize(2)
       for side in range(4):                     #draws a Square as Boundary
              turtle.forward(600)
              turtle.left(90)
       turtle.hideturtle()
       turtle.penup()     

#Main function
def main():
       turtle.speed(0)
       bird_selector()
       turtle_selector()
       text()
       turtle.colormode(255)
       screen.bgcolor("#ffca9a")
       screen.title("Welcome to the Forest Drawing!")
       boundary()                       
       turtle.onscreenclick(handle_click)               
       turtle.register_shape('bird', ((-22,-39),(-20,-7),(-7,3),(-11,7),(-12,9),(-11,10),(-9,10),(-3,7),
              (10,24),(30,16),(13,18),(4,0),(14,-6),(6,-13),(0,-4),(-14,-13),(-22,-39)))     #turtle Registers birds shape
       #turtle.shape('bird')                             #selecting turtle shape to bird
       #turtle.onclick(handle_click)
       turtle.listen(turnleft)                          
       turtle.listen(turnright) 
       turtle.onkey(turnleft,"Left")
       turtle.onkey(turnright,"Right")
       turtle.mainloop()
       return "EVENTLOOP"

#function for handling the mouse clicks on screen
def handle_click(x,y):                                         #handle click will receives (x,y) location of click point
       if (x >-280 and x <300) and (y< 50 and y >-300):        #checks if x and y coordinates of mouse click are inside boundary and quadrant 1 ,4
              turtle.goto(x,y)                                 #turtle will goto accodring to its coordinates
              turtle.hideturtle()                              #hides the turtle()
              tree(x,y)                               #stamps the tree on the screen where the mouse is click
       elif (x <300 and x >-300) and (y< 300 and y >50):       #checks if x and y coordinates of mouse click are inside boundary and quadrant 2 ,3
              turtle.goto(x,y)                                 #turtle will goto accodring to its coordinates
              turtle.hideturtle()                              #hides the turtle()
              stamp_bird(x,y)                                  #stamps the bird on the screen where the mouse is click
       else:                                                   #if click is not inside boundary then numinput will invoke
              turtle.numinput("Warning!", "Click Inside Boundary \n Enter 1 to continue", minval=1, maxval=1) #warning sign, lets user know to click inside boundary
   

    
       
#function for turning the bird position left     
def turnleft():
       turtle.goto(-300,300)
       turtle.fillcolor('purple')
       turtle.showturtle()
       left(10)
       

#function for turning the bird position right
def turnright():
       turtle.goto(-300,300)
       turtle.fillcolor('purple')
       turtle.showturtle()
       right(20)
       turtle.tiltangle(10)


if __name__ == '__main__':
    msg = main()




