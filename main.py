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
current_letter = "G"
#-----functions-----

# given a turtle, set that turtle to be shaped by the image file
def reset_apple(active_apple):
  global current_letter
  length = len(letter_list)
  if(length != 0):
    index = rand.randint(0, length-1)
    active_apple.goto(rand.randint(-screen_width/2, screen_width/2), rand.randint(-screen_height/2, screen_height/2))
    current_letter = letter_list.pop(index)
    draw_apple(active_apple, current_letter)


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

def checkA():
  if(current_letter == "A"):
    drop_apple()

def checkB():
  if(current_letter == "B"):
    drop_apple()

def checkC():
  if(current_letter == "C"):
    drop_apple()

def checkD():
  if(current_letter == "D"):
    drop_apple()

def checkE():
  if(current_letter == "E"):
    drop_apple()

def checkF():
  if(current_letter == "F"):
    drop_apple()

def checkG():
  if(current_letter == "G"):
    drop_apple()

def checkH():
  if(current_letter == "H"):
    drop_apple()

def checkI():
  if(current_letter == "I"):
    drop_apple()

def checkJ():
  if(current_letter == "J"):
    drop_apple()

def checkK():
  if(current_letter == "K"):
    drop_apple()

def checkL():
  if(current_letter == "L"):
    drop_apple()

def checkM():
  if(current_letter == "M"):
    drop_apple()

def checkN():
  if(current_letter == "N"):
    drop_apple()

def checkO():
  if(current_letter == "O"):
    drop_apple()

def checkP():
  if(current_letter == "P"):
    drop_apple()

def checkQ():
  if(current_letter == "Q"):
    drop_apple()

def checkR():
  if(current_letter == "R"):
    drop_apple()

def checkS():
  if(current_letter == "S"):
    drop_apple()

def checkT():
  if(current_letter == "T"):
    drop_apple()

def checkU():
  if(current_letter == "U"):
    drop_apple()

def checkV():
  if(current_letter == "V"):
    drop_apple()

def checkW():
  if(current_letter == "W"):
    drop_apple()

def checkX():
  if(current_letter == "X"):
    drop_apple()

def checkY():
  if(current_letter == "Y"):
    drop_apple()

def checkZ():
  if(current_letter == "Z"):
    drop_apple()

#-----function calls-----
draw_apple(apple, "G")
wn.onkeypress(checkA, "a")
wn.onkeypress(checkB, "b")
wn.onkeypress(checkC, "c")
wn.onkeypress(checkD, "d")
wn.onkeypress(checkE, "e")
wn.onkeypress(checkF, "f")
wn.onkeypress(checkG, "g")
wn.onkeypress(checkH, "h")
wn.onkeypress(checkI, "i")
wn.onkeypress(checkJ, "j")
wn.onkeypress(checkK, "k")
wn.onkeypress(checkL, "l")
wn.onkeypress(checkM, "m")
wn.onkeypress(checkN, "n")
wn.onkeypress(checkO, "o")
wn.onkeypress(checkP, "p")
wn.onkeypress(checkQ, "q")
wn.onkeypress(checkR, "r")
wn.onkeypress(checkS, "s")
wn.onkeypress(checkT, "t")
wn.onkeypress(checkU, "u")
wn.onkeypress(checkV, "v")
wn.onkeypress(checkW, "w")
wn.onkeypress(checkX, "x")
wn.onkeypress(checkY, "y")
wn.onkeypress(checkZ, "z")
wn.listen()
wn.mainloop()