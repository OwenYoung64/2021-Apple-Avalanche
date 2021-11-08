#   a123_apple_1.py
import turtle as trtl
import random as rand
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
fontsetup = "Arial, 12"
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()
wn.tracer(False)
screen_width = 400
screen_height = 400
letter_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
xoffset = -20
yoffset = -47

#-----functions-----

# given a turtle, set that turtle to be shaped by the image file
def reset_apple(active_apple):
  length = len(letter_list)
  if(length != 0):
    index = rand.randint(0, length)
    active_apple.goto(rand.randint(-screen_width/2, screen_width/2), rand.randint(-screen_height/2, screen_height/2))
    draw_apple(active_apple, letter_list.pop(index))


def draw_apple(active_apple, letter):
  active_apple.penup()
  active_apple.shape(apple_image)
  active_apple.showturtle()
  draw_letter(letter, active_apple)
  wn.update()

def drop_apple():
  wn.tracer(True)
  apple.penup()
  apple.goto(apple.xcor(), -160)
  apple.hideturtle()
  apple.clear()
  wn.tracer(False)
  reset_apple(apple)

def draw_letter(letter, active_apple):
  active_apple.color("white")
  remember_pos = active_apple.position()
  active_apple.setpos(active_apple.xcor() + xoffset, active_apple.ycor() + yoffset)
  active_apple.write(letter, font=("Arial", 50, "bold"))
  active_apple.setpos(remember_pos)

#-----function calls-----
draw_apple(apple, "G")
wn.onkeypress(drop_apple, "a")
wn.listen()
wn.mainloop()