from turtle import * 

#we want to paint a castle

#step 1: draw a square
speed(30)
width(7)
color("grey")
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

forward(75)
color("brown")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,200)
pendown()

color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a square












































exitonclick()