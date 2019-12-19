#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
# Daniel A.
#Date
#11/19/19


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl #importing the trtl

#create turtle
sget = trtl.Turtle() #making the trtle


#movement functions
#making the forward option
def up():
    sget.setheading(90)
    sget.forward(9)

#making the right option
def right():
    sget.setheading(0)
    sget.forward(9)

#making the left option
def left():
    sget.setheading(180)
    sget.forward(9)

#making the downward option
def down():
    sget.setheading(270)
    sget.forward(9)

#making the space/reset option
def space():
    sget.clear()


#making the huge/bigger option
def huge():
    sget.width(amount + 1)
    
#making the small/smaller option
def small():
    sget.width(amount - 1)

#making the go up and down option
def PD():
    if sget.penup():
        sget.isdown()
    else:
            sget.isdown()





#color/drawing functions
sget.color("midnightblue") #chaning the color
sget.pensize(1) #the original pensize


amount = 1

#create screen
sget.penup()    #moveing the trtl to a 0
sget.goto(0,0)  #moveing the trtl to a 0
sget.pendown()  #moveing the trtl to a 0

#bind to keypresses


#listen

#mainloop
wn = trtl.Screen()
wn.onkeypress(up,"Up")    #uses the keyboard keys for movement
wn.onkeypress(right,"Right")  #uses the keyboard keys for movement
wn.onkeypress(left,"Left") #uses the keyboard keys for movement
wn.onkeypress(down,"Down")    #uses the keyboard keys for movement
wn.onkeypress(space, "space")   #uses the keyboard keys to delete the drawing
wn.onkeypress(huge,"o")      #uses the keyboard keys to chnage the size
wn.onkeypress(small,"p")     #uses the keyboard keys to chnage the size
wn.onkeypress(PD,"u")     #uses the keyboard keys to move the trtl
wn.listen()
wn.bgcolor("beige") #background color
wn.mainloop() 