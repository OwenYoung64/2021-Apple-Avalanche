#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()

#-----functions-----

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def apple_drop():
  apple.penup()
  apple.goto(active_apple.xcor(), -160)

def draw_an_A():
  apple.color("white")
  apple.write("A", font=("Arial", 74, "bold"))


#-----function calls-----
draw_an_A(apple)
draw_apple(apple)
apple_drop(apple)
wn.mainloop()