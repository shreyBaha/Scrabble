import Scrabble
from tkinter import *

def clear_blocks(placed_block_arr):
  for x in range(0,len(placed_block_arr)):
    i = (int)(placed_block_arr[x][0:placed_block_arr[x].index("-")])
    j = (int)(placed_block_arr[x][placed_block_arr[x].index("-")+1:])
    board_arr[i][j].config(text="")
    board_tile = Scrabble.scrabble_board[i][j]
    board_tile.block = None
    board_tile.occ = False
    if(i != 7 or j != 7):
      board_tile.valid_placement = False
  #above section blocks below section clears valid placement of surrounding blocks
  for i in range(0,15):
    for j in range(0,15):
      if(Scrabble.scrabble_board[i][j].occ == False and (i != 7 or j != 7)):
        if(i > 0 and Scrabble.scrabble_board[i-1][j].occ == True):
          Scrabble.scrabble_board[i][j].valid_placement = True
        elif(i < 14 and Scrabble.scrabble_board[i+1][j].occ == True):
          Scrabble.scrabble_board[i][j].valid_placement = True
        elif(j > 0 and Scrabble.scrabble_board[i][j-1].occ == True):
          Scrabble.scrabble_board[i][j].valid_placement = True
        elif(j < 14 and Scrabble.scrabble_board[i][j+1].occ == True):
          Scrabble.scrabble_board[i][j].valid_placement = True 
        else:
          Scrabble.scrabble_board[i][j].valid_placement = False

def check_word():
  if(Scrabble.p1turn):
    hide_let(player1_arr)
  else:
    hide_let(player2_arr)
  if(len(placed_block_arr) != 0):
    #make check if i > 0 ect in case of index out of bounds
    if(len(placed_block_arr) == 1 and (int)(placed_block_arr[0][0:placed_block_arr[0].index("-")]) < 14 and (Scrabble.scrabble_board[(int)(placed_block_arr[0][0:placed_block_arr[0].index("-")])+1][(int)(placed_block_arr[0][placed_block_arr[0].index("-")+1:])].occ)):
      #print("vert")
      score = Scrabble.get_score((int)(placed_block_arr[0][0:placed_block_arr[0].index("-")]), (int)(placed_block_arr[0][placed_block_arr[0].index("-")+1:]), False)
    elif(len(placed_block_arr) == 1 and (int)(placed_block_arr[0][0:placed_block_arr[0].index("-")]) > 0 and Scrabble.scrabble_board[(int)(placed_block_arr[0][0:placed_block_arr[0].index("-")])-1][(int)(placed_block_arr[0][placed_block_arr[0].index("-")+1:])].occ):
      #print("vert")
      score = Scrabble.get_score((int)(placed_block_arr[0][0:placed_block_arr[0].index("-")]), (int)(placed_block_arr[0][placed_block_arr[0].index("-")+1:]), False)
    elif(len(placed_block_arr) == 1 and (int)(placed_block_arr[0][placed_block_arr[0].index("-")+1:]) < 14 and (Scrabble.scrabble_board[(int)(placed_block_arr[0][0:placed_block_arr[0].index("-")])][(int)(placed_block_arr[0][placed_block_arr[0].index("-")+1:])+1].occ)):
      #print("hor")
      score = Scrabble.get_score((int)(placed_block_arr[0][0:placed_block_arr[0].index("-")]), (int)(placed_block_arr[0][placed_block_arr[0].index("-")+1:]), True)
    elif(len(placed_block_arr) == 1 and (int)(placed_block_arr[0][placed_block_arr[0].index("-")+1:]) < 14 and Scrabble.scrabble_board[(int)(placed_block_arr[0][0:placed_block_arr[0].index("-")])][(int)(placed_block_arr[0][placed_block_arr[0].index("-")+1:])-1].occ):
      #print("hor")
      score = Scrabble.get_score((int)(placed_block_arr[0][0:placed_block_arr[0].index("-")]), (int)(placed_block_arr[0][placed_block_arr[0].index("-")+1:]), True)
    elif(len(placed_block_arr) > 1 and (int)(placed_block_arr[0][0:placed_block_arr[0].index("-")]) == (int)(placed_block_arr[1][0:placed_block_arr[1].index("-")])):
      score = Scrabble.get_score((int)(placed_block_arr[0][0:placed_block_arr[0].index("-")]), (int)(placed_block_arr[0][placed_block_arr[0].index("-")+1:]), True)
      #print("hor")
    else:
      #print("vert")
      score = Scrabble.get_score((int)(placed_block_arr[0][0:placed_block_arr[0].index("-")]), (int)(placed_block_arr[0][placed_block_arr[0].index("-")+1:]), False)
    #print(score)
    if(score != None): # if word doesn't exit clear blocks from display || change this to None down the line
      update_score(score)
      for i in placed_widget_arr:
        #print(placed_widget_arr)
        #print("1")
        pick_block(i)
    else:
      clear_blocks(placed_block_arr)
  update_board()
      
  placed_block_arr.clear()
  placed_widget_arr.clear()
  Scrabble.p1turn = not Scrabble.p1turn
  update_turn_label()

def update_turn_label():
  if(Scrabble.p1turn):
    turn_display.config(text="P1 turn")
  else:
    turn_display.config(text="P2 turn")

def p1display():
  if(Scrabble.p1turn): 
    for i in player1_arr:
      if(not i.cget("text") == ""):
        i.config(fg="black")
        i.bind("<Button-1>", drag_start) #add if statement to see if i has a text to know if it shiuld be unbinded and if the turn allows it//make a label that displays whos turn it is
        i.bind("<B1-Motion>", drag_motion)
        i.bind("<ButtonRelease-1>", drag_stop)

def p2display():
  if(not Scrabble.p1turn):
    for i in player2_arr:
      if(not i.cget("text") == ""):
        i.config(fg="black")
        i.bind("<Button-1>", drag_start)
        i.bind("<B1-Motion>", drag_motion)
        i.bind("<ButtonRelease-1>", drag_stop)

def hide_let(arr):
  for i in arr:
    i.config(fg="white")
    i.unbind("<Button-1>", funcid=None)
    i.unbind("<B1-Motion>", funcid=None)
    i.unbind("<ButtonRelease-1>", funcid=None)

def update_score(num):
  if(Scrabble.p1turn):
    new_score = (int)(scorep1.cget("text")[10:]) + num
    scorep1.config(text=f"Score P1: {new_score}")
  else:
    new_score = (int)(scorep2.cget("text")[10:]) + num
    scorep2.config(text=f"Score P2: {new_score}")
    
def update_board():
  for i in range(0, 15):
    for j in range(0, 15):
      labell = board_arr[i][j]
      if(Scrabble.scrabble_board[i][j].mult_let == 2):
        labell.config(bg="light blue")
        if(labell.cget("text") == ""):
          labell.config(text="x2")
      elif(Scrabble.scrabble_board[i][j].mult_let == 3):
       labell.config(bg="blue")
       if(labell.cget("text") == ""):
          labell.config(text= "x3")
      elif(Scrabble.scrabble_board[i][j].mult_word == 3):
        labell.config(bg="red")
        if(labell.cget("text") == ""):
          labell.config(text= "x3")
      elif(Scrabble.scrabble_board[i][j].mult_word == 2):
        labell.config(bg="orange")
        if(labell.cget("text") == ""):
          labell.config(text="x2")
      elif(Scrabble.scrabble_board[i][j].valid_placement == True):
        labell.config(bg="beige")
      else:
        labell.config(bg="light grey")

def return_block(p1turn, widget):
  if(p1turn):
    for i in range(0,7):
      if(player1_arr[i] == widget):
        widget.place(x=219.5+i*48, y=600)
  else:
   for i in range(0,7):
      if(player2_arr[i] == widget):
        widget.place(x=219.5+i*48, y=650) 
  widget.config(fg="white")
  widget.unbind("<Button-1>", funcid=None)
  widget.unbind("<B1-Motion>", funcid=None)
  widget.unbind("<ButtonRelease-1>", funcid=None)
          

def pick_block(widget):
  #print(len(Scrabble.block_bag))
  if(len(Scrabble.block_bag) != 0):
    #print("2")
    widget.config(text=Scrabble.block_bag.pop().letter)
  else:     #else remove text and unbind the widget if bag is empty (no more blocks to draw)
    #print("3")
    widget.config(text="")
    widget.unbind("<Button-1>", funcid=None)
    widget.unbind("<B1-Motion>", funcid=None)
    widget.unbind("<ButtonRelease-1>", funcid=None)


def drag_start(event):
  widget = event.widget
  widget.startx = event.x
  widget.starty = event.y

def drag_motion(event):
  widget = event.widget
  x = widget.winfo_x() - widget.startx + event.x 
  y = widget.winfo_y() - widget.starty + event.y
  widget.place(x=x, y=y)
  x = widget.winfo_x()+20
  y = widget.winfo_y()+20
  print((str)(x)+", "+(str)(y)) #location of top left corner. need to make the coordinates give pos of middle
   
   
   #j and i reversed in this method
def drag_stop(event):
  widget = event.widget
  x = widget.winfo_x()+20
  y = widget.winfo_y()+20
  for i in range(0, 15):
    for j in range(0, 15):
      if(x > 25+48*i and x < 25+48*(i+1) and y > 40*j and y < 40*(j+1)):
        if(Scrabble.scrabble_board[j][i].occ == False):
          Scrabble.place_block(Scrabble.Block(widget.cget("text").lower()), j, i)
          if(Scrabble.scrabble_board[j][i].block != None):
            placed_block_arr.append(f"{j}-{i}")
            update_board() # call made to update beige blocks
            board_arr[j][i].config(text=widget.cget("text"))
            placed_widget_arr.append(widget)  
            return_block(Scrabble.p1turn, widget)
            #print(int(placed_block_arr[0][0:placed_block_arr[0].index("-")]))
            #print(int(placed_block_arr[0][placed_block_arr[0].index("-")+1:]))
            #print(placed_block_arr)

root = Tk()

root.geometry("775x700")
root.title("Scrabble")
board_frame = LabelFrame(root, width = 600, height = 600, bg="grey")
board_frame.place(x=25, y = 0)
player_frame = LabelFrame(root, height=40, width=336)
player_frame.place(x=219.5, y=600)
scorep1 = Label(root, padx= 20, pady= 10, text="Score P1: 0", bg="yellow")
scorep1.place(x=100, y=600)
scorep2 = Label(root, padx= 20, pady= 10, text="Score P2: 0", bg="yellow")
scorep2.place(x=100, y=650)
player1_arr = []
player2_arr = []
player1_display = Button(root, width=7, height= 1, text= "P1 Display", command=p1display)
player1_display.place(x=610, y=600)
player2_display = Button(root, width=7, height= 1, text= "P2 Display", command=p2display)
player2_display.place(x=610, y=650)
turn_display = Label(root, text="P1 turn", width=7, height=1)
turn_display.place(x=700,y=600)
check = Button(root, width=7, height= 1, text= "check word", command=check_word)
check.place(x=700,y=650)
placed_block_arr = []
placed_widget_arr = []

p2hide = LabelFrame()
for i in range(0, 7):
  x = LabelFrame(root, width=48, height=40, bg="white", text=Scrabble.block_bag.pop().letter)
  x.place(x=219.5+i*48, y=600)
  x.bind("<Button-1>", drag_start)
  x.bind("<B1-Motion>", drag_motion)
  x.bind("<ButtonRelease-1>", drag_stop)
  player1_arr.append(x)
for i in range(0, 7):
  x = LabelFrame(root, width=48, height=40, bg="white", text=Scrabble.block_bag.pop().letter)
  x.place(x=219.5+i*48, y=650)
  x.bind("<Button-1>", drag_start)
  x.bind("<B1-Motion>", drag_motion)
  x.bind("<ButtonRelease-1>", drag_stop)
  player2_arr.append(x)
  hide_let(player2_arr)

board0000 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0001 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0002 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0003 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0004 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0005 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0006 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0007 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0008 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0009 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0010 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0011 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0012 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0013 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0014 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0100 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0101 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0102 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0103 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0104 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0105 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0106 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0107 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0108 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0109 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0110 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0111 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0112 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0113 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0114 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0200 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0201 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0202 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0203 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0204 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0205 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0206 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0207 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0208 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0209 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0210 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0211 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0212 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0213 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0214 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0300 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0301 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0302 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0303 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0304 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0305 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0306 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0307 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0308 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0309 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0310 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0311 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0312 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0313 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0314 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0400 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0401 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0402 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0403 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0404 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0405 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0406 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0407 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0408 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0409 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0410 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0411 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0412 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0413 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0414 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0500 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0501 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0502 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0503 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0504 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0505 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0506 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0507 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0508 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0509 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0510 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0511 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0512 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0513 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0514 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0600 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0601 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0602 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0603 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0604 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0605 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0606 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0607 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0608 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0609 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0610 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0611 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0612 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0613 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0614 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0700 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0701 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0702 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0703 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0704 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0705 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0706 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0707 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0708 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0709 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0710 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0711 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0712 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0713 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0714 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0800 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0801 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0802 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0803 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0804 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0805 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0806 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0807 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0808 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0809 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0810 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0811 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0812 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0813 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0814 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0900 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0901 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0902 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0903 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0904 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0905 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0906 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0907 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0908 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0909 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0910 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0911 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0912 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0913 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board0914 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1000 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1001 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1002 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1003 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1004 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1005 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1006 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1007 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1008 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1009 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1010 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1011 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1012 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1013 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1014 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1100 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1101 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1102 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1103 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1104 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1105 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1106 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1107 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1108 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1109 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1110 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1111 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1112 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1113 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1114 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1200 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1201 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1202 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1203 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1204 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1205 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1206 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1207 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1208 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1209 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1210 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1211 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1212 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1213 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1214 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1300 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1301 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1302 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1303 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1304 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1305 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1306 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1307 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1308 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1309 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1310 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1311 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1312 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1313 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1314 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1400 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1401 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1402 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1403 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1404 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1405 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1406 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1407 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1408 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1409 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1410 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1411 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1412 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1413 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)
board1414 = Label(board_frame, padx=18, pady=12, bg="white", borderwidth=0, highlightthickness=0)


board0000.grid(row = 0, column = 0)
board0001.grid(row = 0, column = 1)
board0002.grid(row = 0, column = 2)
board0003.grid(row = 0, column = 3)
board0004.grid(row = 0, column = 4)
board0005.grid(row = 0, column = 5)
board0006.grid(row = 0, column = 6)
board0007.grid(row = 0, column = 7)
board0008.grid(row = 0, column = 8)
board0009.grid(row = 0, column = 9)
board0010.grid(row = 0, column = 10)
board0011.grid(row = 0, column = 11)
board0012.grid(row = 0, column = 12)
board0013.grid(row = 0, column = 13)
board0014.grid(row = 0, column = 14)
board0100.grid(row = 1, column = 0)
board0101.grid(row = 1, column = 1)
board0102.grid(row = 1, column = 2)
board0103.grid(row = 1, column = 3)
board0104.grid(row = 1, column = 4)
board0105.grid(row = 1, column = 5)
board0106.grid(row = 1, column = 6)
board0107.grid(row = 1, column = 7)
board0108.grid(row = 1, column = 8)
board0109.grid(row = 1, column = 9)
board0110.grid(row = 1, column = 10)
board0111.grid(row = 1, column = 11)
board0112.grid(row = 1, column = 12)
board0113.grid(row = 1, column = 13)
board0114.grid(row = 1, column = 14)
board0200.grid(row = 2, column = 0)
board0201.grid(row = 2, column = 1)
board0202.grid(row = 2, column = 2)
board0203.grid(row = 2, column = 3)
board0204.grid(row = 2, column = 4)
board0205.grid(row = 2, column = 5)
board0206.grid(row = 2, column = 6)
board0207.grid(row = 2, column = 7)
board0208.grid(row = 2, column = 8)
board0209.grid(row = 2, column = 9)
board0210.grid(row = 2, column = 10)
board0211.grid(row = 2, column = 11)
board0212.grid(row = 2, column = 12)
board0213.grid(row = 2, column = 13)
board0214.grid(row = 2, column = 14)
board0300.grid(row = 3, column = 0)
board0301.grid(row = 3, column = 1)
board0302.grid(row = 3, column = 2)
board0303.grid(row = 3, column = 3)
board0304.grid(row = 3, column = 4)
board0305.grid(row = 3, column = 5)
board0306.grid(row = 3, column = 6)
board0307.grid(row = 3, column = 7)
board0308.grid(row = 3, column = 8)
board0309.grid(row = 3, column = 9)
board0310.grid(row = 3, column = 10)
board0311.grid(row = 3, column = 11)
board0312.grid(row = 3, column = 12)
board0313.grid(row = 3, column = 13)
board0314.grid(row = 3, column = 14)
board0400.grid(row = 4, column = 0)
board0401.grid(row = 4, column = 1)
board0402.grid(row = 4, column = 2)
board0403.grid(row = 4, column = 3)
board0404.grid(row = 4, column = 4)
board0405.grid(row = 4, column = 5)
board0406.grid(row = 4, column = 6)
board0407.grid(row = 4, column = 7)
board0408.grid(row = 4, column = 8)
board0409.grid(row = 4, column = 9)
board0410.grid(row = 4, column = 10)
board0411.grid(row = 4, column = 11)
board0412.grid(row = 4, column = 12)
board0413.grid(row = 4, column = 13)
board0414.grid(row = 4, column = 14)
board0500.grid(row = 5, column = 0)
board0501.grid(row = 5, column = 1)
board0502.grid(row = 5, column = 2)
board0503.grid(row = 5, column = 3)
board0504.grid(row = 5, column = 4)
board0505.grid(row = 5, column = 5)
board0506.grid(row = 5, column = 6)
board0507.grid(row = 5, column = 7)
board0508.grid(row = 5, column = 8)
board0509.grid(row = 5, column = 9)
board0510.grid(row = 5, column = 10)
board0511.grid(row = 5, column = 11)
board0512.grid(row = 5, column = 12)
board0513.grid(row = 5, column = 13)
board0514.grid(row = 5, column = 14)
board0600.grid(row = 6, column = 0)
board0601.grid(row = 6, column = 1)
board0602.grid(row = 6, column = 2)
board0603.grid(row = 6, column = 3)
board0604.grid(row = 6, column = 4)
board0605.grid(row = 6, column = 5)
board0606.grid(row = 6, column = 6)
board0607.grid(row = 6, column = 7)
board0608.grid(row = 6, column = 8)
board0609.grid(row = 6, column = 9)
board0610.grid(row = 6, column = 10)
board0611.grid(row = 6, column = 11)
board0612.grid(row = 6, column = 12)
board0613.grid(row = 6, column = 13)
board0614.grid(row = 6, column = 14)
board0700.grid(row = 7, column = 0)
board0701.grid(row = 7, column = 1)
board0702.grid(row = 7, column = 2)
board0703.grid(row = 7, column = 3)
board0704.grid(row = 7, column = 4)
board0705.grid(row = 7, column = 5)
board0706.grid(row = 7, column = 6)
board0707.grid(row = 7, column = 7)
board0708.grid(row = 7, column = 8)
board0709.grid(row = 7, column = 9)
board0710.grid(row = 7, column = 10)
board0711.grid(row = 7, column = 11)
board0712.grid(row = 7, column = 12)
board0713.grid(row = 7, column = 13)
board0714.grid(row = 7, column = 14)
board0800.grid(row = 8, column = 0)
board0801.grid(row = 8, column = 1)
board0802.grid(row = 8, column = 2)
board0803.grid(row = 8, column = 3)
board0804.grid(row = 8, column = 4)
board0805.grid(row = 8, column = 5)
board0806.grid(row = 8, column = 6)
board0807.grid(row = 8, column = 7)
board0808.grid(row = 8, column = 8)
board0809.grid(row = 8, column = 9)
board0810.grid(row = 8, column = 10)
board0811.grid(row = 8, column = 11)
board0812.grid(row = 8, column = 12)
board0813.grid(row = 8, column = 13)
board0814.grid(row = 8, column = 14)
board0900.grid(row = 9, column = 0)
board0901.grid(row = 9, column = 1)
board0902.grid(row = 9, column = 2)
board0903.grid(row = 9, column = 3)
board0904.grid(row = 9, column = 4)
board0905.grid(row = 9, column = 5)
board0906.grid(row = 9, column = 6)
board0907.grid(row = 9, column = 7)
board0908.grid(row = 9, column = 8)
board0909.grid(row = 9, column = 9)
board0910.grid(row = 9, column = 10)
board0911.grid(row = 9, column = 11)
board0912.grid(row = 9, column = 12)
board0913.grid(row = 9, column = 13)
board0914.grid(row = 9, column = 14)
board1000.grid(row = 10, column = 0)
board1001.grid(row = 10, column = 1)
board1002.grid(row = 10, column = 2)
board1003.grid(row = 10, column = 3)
board1004.grid(row = 10, column = 4)
board1005.grid(row = 10, column = 5)
board1006.grid(row = 10, column = 6)
board1007.grid(row = 10, column = 7)
board1008.grid(row = 10, column = 8)
board1009.grid(row = 10, column = 9)
board1010.grid(row = 10, column = 10)
board1011.grid(row = 10, column = 11)
board1012.grid(row = 10, column = 12)
board1013.grid(row = 10, column = 13)
board1014.grid(row = 10, column = 14)
board1100.grid(row = 11, column = 0)
board1101.grid(row = 11, column = 1)
board1102.grid(row = 11, column = 2)
board1103.grid(row = 11, column = 3)
board1104.grid(row = 11, column = 4)
board1105.grid(row = 11, column = 5)
board1106.grid(row = 11, column = 6)
board1107.grid(row = 11, column = 7)
board1108.grid(row = 11, column = 8)
board1109.grid(row = 11, column = 9)
board1110.grid(row = 11, column = 10)
board1111.grid(row = 11, column = 11)
board1112.grid(row = 11, column = 12)
board1113.grid(row = 11, column = 13)
board1114.grid(row = 11, column = 14)
board1200.grid(row = 12, column = 0)
board1201.grid(row = 12, column = 1)
board1202.grid(row = 12, column = 2)
board1203.grid(row = 12, column = 3)
board1204.grid(row = 12, column = 4)
board1205.grid(row = 12, column = 5)
board1206.grid(row = 12, column = 6)
board1207.grid(row = 12, column = 7)
board1208.grid(row = 12, column = 8)
board1209.grid(row = 12, column = 9)
board1210.grid(row = 12, column = 10)
board1211.grid(row = 12, column = 11)
board1212.grid(row = 12, column = 12)
board1213.grid(row = 12, column = 13)
board1214.grid(row = 12, column = 14)
board1300.grid(row = 13, column = 0)
board1301.grid(row = 13, column = 1)
board1302.grid(row = 13, column = 2)
board1303.grid(row = 13, column = 3)
board1304.grid(row = 13, column = 4)
board1305.grid(row = 13, column = 5)
board1306.grid(row = 13, column = 6)
board1307.grid(row = 13, column = 7)
board1308.grid(row = 13, column = 8)
board1309.grid(row = 13, column = 9)
board1310.grid(row = 13, column = 10)
board1311.grid(row = 13, column = 11)
board1312.grid(row = 13, column = 12)
board1313.grid(row = 13, column = 13)
board1314.grid(row = 13, column = 14)
board1400.grid(row = 14, column = 0)
board1401.grid(row = 14, column = 1)
board1402.grid(row = 14, column = 2)
board1403.grid(row = 14, column = 3)
board1404.grid(row = 14, column = 4)
board1405.grid(row = 14, column = 5)
board1406.grid(row = 14, column = 6)
board1407.grid(row = 14, column = 7)
board1408.grid(row = 14, column = 8)
board1409.grid(row = 14, column = 9)
board1410.grid(row = 14, column = 10)
board1411.grid(row = 14, column = 11)
board1412.grid(row = 14, column = 12)
board1413.grid(row = 14, column = 13)
board1414.grid(row = 14, column = 14)


board_arr = [[board0000, board0001, board0002, board0003, board0004, board0005, board0006, board0007, board0008, board0009, board0010, board0011, board0012, board0013, board0014],
[board0100, board0101, board0102, board0103, board0104, board0105, board0106, board0107, board0108, board0109, board0110, board0111, board0112, board0113, board0114],
[board0200, board0201, board0202, board0203, board0204, board0205, board0206, board0207, board0208, board0209, board0210, board0211, board0212, board0213, board0214],
[board0300, board0301, board0302, board0303, board0304, board0305, board0306, board0307, board0308, board0309, board0310, board0311, board0312, board0313, board0314],
[board0400, board0401, board0402, board0403, board0404, board0405, board0406, board0407, board0408, board0409, board0410, board0411, board0412, board0413, board0414],
[board0500, board0501, board0502, board0503, board0504, board0505, board0506, board0507, board0508, board0509, board0510, board0511, board0512, board0513, board0514],
[board0600, board0601, board0602, board0603, board0604, board0605, board0606, board0607, board0608, board0609, board0610, board0611, board0612, board0613, board0614],             
[board0700, board0701, board0702, board0703, board0704, board0705, board0706, board0707, board0708, board0709, board0710, board0711, board0712, board0713, board0714],
[board0800, board0801, board0802, board0803, board0804, board0805, board0806, board0807, board0808, board0809, board0810, board0811, board0812, board0813, board0814],
[board0900, board0901, board0902, board0903, board0904, board0905, board0906, board0907, board0908, board0909, board0910, board0911, board0912, board0913, board0914],
[board1000, board1001, board1002, board1003, board1004, board1005, board1006, board1007, board1008, board1009, board1010, board1011, board1012, board1013, board1014],
[board1100, board1101, board1102, board1103, board1104, board1105, board1106, board1107, board1108, board1109, board1110, board1111, board1112, board1113, board1114],
[board1200, board1201, board1202, board1203, board1204, board1205, board1206, board1207, board1208, board1209, board1210, board1211, board1212, board1213, board1214],
[board1300, board1301, board1302, board1303, board1304, board1305, board1306, board1307, board1308, board1309, board1310, board1311, board1312, board1313, board1314],
[board1400, board1401, board1402, board1403, board1404, board1405, board1406, board1407, board1408, board1409, board1410, board1411, board1412, board1413, board1414],
]

update_board()

root.mainloop()