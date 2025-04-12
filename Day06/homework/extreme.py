from turtle import *

bgcolor("sky blue")
title("Sky scene with turtle")
speed(100)
#draw castle

penup()
goto(-100,-100)
pendown()

width(7)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(55)
color("brown")
begin_fill()
left(90)
forward(90)
right(90)
forward(90)
right(90)
forward(90)
end_fill()

penup()
goto(100,100)
pendown()

color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing the windows

width(3)
penup()
goto(80,80)
pendown()

right(60)
forward(60)
left(90)
forward(80)
left(90)
forward(60)
left(90)
forward(80)

penup()
goto(50,80)
pendown()
left(180)
forward(80)

penup()
goto(20,40)
pendown()
left(90)
forward(60)


penup()
goto(-80,80)
pendown()
forward(60)
right(90)
forward(80)
right(90)
forward(60)
right(90)
forward(80)

penup()
goto(-50,80)
pendown()
right(180)
forward(80)

penup()
goto(-20,40)
pendown()
right(90)
forward(60)

#drawing the sun
penup()
goto(-500,270)
pendown()
color("yellow")
begin_fill()

def draw_circle(radius):
    pendown()
    circle(radius)
    penup()

#set up the turtle

penup()
goto(-500,270)

draw_circle(50)
end_fill()

#rays
num_rays = 12     #number of rays
ray_lenth = 30

for i in range(num_rays):
    #print(i)
    penup()
    goto(-500,215)

    setheading(i*(360/num_rays))
    forward(60)
    pendown()
    forward(30)


penup()
goto(-320,220)
pendown()

#cloud
color("white","white")
begin_fill()
circle(25)
end_fill()

def filled_circle(rds,clr):
    color(clr,clr)
    begin_fill()
    circle(rds)
    end_fill()

filled_circle(25,"white")

radius = 25
cloud_color="white"

filled_circle(radius,cloud_color)

forward(radius)
filled_circle(radius,cloud_color)
right(90)
filled_circle(radius,cloud_color)
right(90)
filled_circle(radius,cloud_color)
right(90)
filled_circle(radius,cloud_color)
right(90)

def cloud(radius,cloud_color="white"):
    filled_circle(radius,cloud_color)
    forward(radius)
    filled_circle(radius,cloud_color)
    right(90)
    filled_circle(radius,cloud_color)
    right(90)
    filled_circle(radius,cloud_color)
    right(90)
    filled_circle(radius,cloud_color)
    right(90)

radius = 25

cloud(radius)

penup()
goto(350,220)
pendown()

cloud(radius)

#draw the grass

def drawgrass():
    color('green')
    shape('square')
    penup()
    goto(0,-300)
    shapesize(20,80)
    right(150)
    stamp()

drawgrass()

exitonclick()
