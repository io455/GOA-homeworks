from turtle import*
width=800
height=600
setup(width, height)
bgcolor("lightblue")
speed(150)
#draw castle
def draw_rectangle(width, height):
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)

def draw_castle():
    #ვხატავ კვადრატულ ფუძეს ანუ მთავარ სასახლეს
    penup()
    goto(-150, -150)
    pendown()
    color("black", "grey")
    begin_fill()
    draw_rectangle(300, 300)
    end_fill()
    tower_radius = 40
    positions = [(-150, -150), (150, -150), (150, 150), (-150, 150)]
    for pos in positions:
        penup()
        goto(pos[0] + tower_radius, pos[1] - tower_radius)
        pendown()
        color("black", "darkgrey")
        begin_fill()
        circle(tower_radius)
        end_fill()
penup()
goto(-180, -180)
pendown()
color("blue")
for _ in range(4):
    print(_)
    forward(360)
    left(90)
hideturtle

draw_castle()
exitonclick()




