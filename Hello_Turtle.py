# Hello_Turtle.py
#    This program demonstrates turtle graphics library.
#    Written by Chris Everett, August 31, 2019. Sierra College IT 0075 - Data Analytics Program
#    I used "https://docs.python.org/3/library/turtle.html" as a reference.
#    "Turtles, all the way down."

import turtle    # Imports turtle graphics library

def main():    # Defines main program function
    # In lab I typed my_turtle 102 times so object is now "m_turt"
    m_turt = turtle.Turtle()     # Creates a turtle graphics window
    m_turt.screen.title("Hello Turtle - Demonstration")    # Names window; google search for method
    m_turt.shape("turtle")    # Courser appears as a small turtle; google search for method
    m_turt.color("green")    # Sets the color of cursor and line

    # Instructions will attempt to draw a large turtle;
    m_turt.up()
    m_turt.right(90)
    m_turt.forward(150)
    m_turt.left(90)
    m_turt.down()
    m_turt.circle(200, 360)    # Body
    m_turt.right(180)
    m_turt.pensize(5)
    m_turt.circle(50, 135)    # Head first half
    m_turt.pensize(1)
    m_turt.color("black")    # Eye
    m_turt.circle(10, 360)
    m_turt.color("green")
    m_turt.pensize(5)
    m_turt.circle(50, 90)
    m_turt.pensize(1)
    m_turt.color("black")    # Eye
    m_turt.circle(10, 360)
    m_turt.color("green")
    m_turt.pensize(5)
    m_turt.circle(50, 135) # Head second half
    m_turt.pensize(1)

    for i in range(4): # Draw four spots; creates a loop where range repeats; from "Python Programing: An Introduction to Computer Science."
         m_turt.right(180)
         m_turt.circle(50, 540)
         m_turt.color("blue")
         m_turt.circle(30, 360)
         m_turt.color("green")

   # It would be easier if each leg and spot generated during initial circle.
   # I want to fill in each segment but fill function will need more work.

    m_turt.left(180)
    m_turt.circle(10, 360)    # Little tail

    # Create loop for below would be nice.

    m_turt.left(180)    # Starts instructions to build feet and spots
    m_turt.circle(200, 45)
    m_turt.right(180)
    m_turt.pensize(5)
    m_turt.circle(30, 360)   # Foot
    m_turt.pensize(1)
    m_turt.right(180)
    m_turt.circle(50, 360)    # Spot
    m_turt.color("blue")
    m_turt.circle(30, 360)
    m_turt.color("green")
    m_turt.circle(200, 45)
    m_turt.circle(50, 360)    # Spot
    m_turt.color("blue")
    m_turt.circle(30, 360)
    m_turt.color("green")
    m_turt.circle(200, 45)
    m_turt.circle(50, 360)    # Spot
    m_turt.color("blue")
    m_turt.circle(30, 360)
    m_turt.color("green")
    m_turt.right(180)
    m_turt.pensize(5)
    m_turt.circle(30, 360)   # Foot
    m_turt.pensize(1)
    m_turt.right(180)

    m_turt.circle(200, 90)    # Move curser to right-side

    m_turt.right(180)    # Starts instructions to build feet and spots
    m_turt.pensize(5)
    m_turt.circle(30, 360)   # Foot
    m_turt.pensize(1)
    m_turt.right(180)
    m_turt.circle(50, 360)    # Spot
    m_turt.color("blue")
    m_turt.circle(30, 360)
    m_turt.color("green")
    m_turt.circle(200, 45)
    m_turt.circle(50, 360)    # Spot
    m_turt.color("blue")
    m_turt.circle(30, 360)
    m_turt.color("green")
    m_turt.circle(200, 45)
    m_turt.circle(50, 360)    # Spot
    m_turt.color("blue")
    m_turt.circle(30, 360)
    m_turt.color("green")
    m_turt.right(180)
    m_turt.pensize(5)
    m_turt.circle(30, 360)   # Foot
    m_turt.pensize(1)
    m_turt.right(180)

    m_turt.pensize(20)
    m_turt.circle(200, 405)    # Create larger circle

    input() # This will pause the program.


main()    # End of main function
