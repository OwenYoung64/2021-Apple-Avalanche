#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
fontsetup = "Arial, 12"
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()
wn.tracer(False)
xoffset = -20
yoffset = -47

#-----functions-----

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.penup()
  active_apple.shape(apple_image)
  draw_letter("A", active_apple)
  wn.update()

def drop_apple():
  wn.tracer(True)
  apple.penup()
  apple.goto(apple.xcor(), -160)
  wn.tracer(False)

def draw_letter(letter, active_apple):
  active_apple.color("white")
  remember_pos = active_apple.position()
  active_apple.setpos(active_apple.xcor() + xoffset, active_apple.ycor() + yoffset)
  active_apple.write(letter, font=("Arial", 50, "bold"))
  active_apple.setpos(remember_pos)


#-----function calls-----
draw_apple(apple)
wn.onkeypress(drop_apple, "a")
wn.listen()
wn.mainloop()