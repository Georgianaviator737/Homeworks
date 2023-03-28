from turtle import *

#house

speed(30)

#step 1: square

width(7)
color("purple")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()

#step 2: door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(100) #door height
right(90)
forward(60)
right(90)
forward(100)
end_fill()

#step 3: roof

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#step 4: right window

penup()
goto(200, 170)
pendown()

color("blue")
begin_fill()
right(60)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#step 5: left window 

penup()
goto(0, 170)
pendown()

color("blue")
begin_fill()
right(0)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

exitonclick()
