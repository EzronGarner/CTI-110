#Ezron Garner
#10/27/26
# P4 LAB1
#Use turtle and loops to draw a square and a triangle


#Import the library
import turtle

#create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()
win.bgcolor("blue")
#Set turtle options
pen.pensize(5)
pen.pencolor("purple")
pen.shape("arrow")


#Code to draw the shapes
for side in range(4):
    pen.forward(100)
    pen.left(90)


#While loop that executes 3 times
sides = 3
pen.left(90)
pen.forward(100)
pen.left(270)



pen.begin_fill()
pen.fillcolor("yellow")

while sides > 0:
   pen.forward(100)
   pen.left(120)
   sides = sides -1

pen.end_fill()



#wait for user to close window
win.mainloop()
