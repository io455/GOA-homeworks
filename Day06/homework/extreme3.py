from turtle import*
speed(150)

#ვაკეთებ მომრგვალებულ კარიბჭეს
def door():
    door_width = 100
    door_height = 150
    arc_radius = door_width/2
    forward(door_width)

    #right(90)
    circle(arc_radius, 180)
    forward(100)
    penup()
    
   
def dome():
    right(90)
    forward(90)
    

    
    
    left(90)
    forward(30)

    left(90)
    forward(30)

    right(90)
    forward(30)

    right(90)
    forward(30)

    left(90)
    forward(30)

    left(90)
    forward(30)

    right(90)
    forward(30)

    right(90)
    forward(30)

    left(90)
    forward(30)
    left(90)
    forward(40)

    left(40)
    forward(80)

   


    

#ვიწყებთ სასახლის შენებას
def castle():
    penup()
    goto(-350, -100)
    pendown()
    color("black")
    begin_fill
    forward(300)
    left(90)
    door()

    goto(-50,-100)
    pendown()

    left(90)
    forward(200)

    left(90)
    forward(250)

    left(320)
    forward(80)

    left(40)
    forward(30)
    
    left(90)
    forward(30)

    left(90)
    forward(30)

    right(90)
    forward(30)

    right(90)
    forward(30)

    left(90)
    forward(30)

    left(90)
    forward(30)

    right(90)
    forward(30)

    right(90)
    forward(30)

    left(90)
    forward(30)

    left(90)
    forward(90)
    right(90)
    forward(100)

    right(90)
    forward(80)
    left(90)
    forward(30)
    right(60)
    forward(80)
    left(120)
    forward(80)
    right(60)
    forward(30)
    left(90)
    forward(80)

    right(90)
    forward(100)
    dome()

    right(35)
    forward(250)

    

    

castle()

exitonclick()

    









