#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.penup()
turtle.forward(100)
turtle.pendown()

turtle.fillcolor(0,255,255)
turtle.begin_fill()
turtle.forward(250)
turtle.left(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(250)       
turtle.left(90)
turtle.forward(250)
turtle.end_fill()


turtle.right(90)
turtle.penup()
turtle.forward(200)        
turtle.pendown()

center_x=0
center_y=0



turtle.color(255,0,0)
x,y=turtle.pos()
center_x+=x
center_y+=y
turtle.width(5)
turtle.right(120)
turtle.forward(50)
x,y=turtle.pos()
center_x+=x
center_y+=y
turtle.right(120)
turtle.forward(50)
x,y=turtle.pos()
center_x+=x
center_y+=y
turtle.right(120)
turtle.forward(50)

center_x/=3
center_y/=3

radius=50
turtle.penup()
turtle.setpos(center_x, center_y+radius)
turtle.pendown()
turtle.color(0,0,255)
turtle.width(2)
turtle.circle(radius)

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.right(90)
turtle.begin_fill()
turtle.end_fill()
turtle.done()