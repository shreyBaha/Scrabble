import numpy as np

class Block:
  def __init__(self, letter):
    self.letter = letter
    let = letter.upper()
    if("AEIOULNSTR".__contains__(let)):
      value = 1
    elif("DG".__contains__(let)):
      value = 2
    elif("BCMP".__contains__(let)):
      value = 3
    elif("FHVWY".__contains__(let)):
      value = 4
    elif("K".__contains__(let)):
      value = 5
    elif("JX".__contains__(let)):
      value = 8
    else:
      value = 10
    self.value = value

class Tile:
  def __init__(self, block, occ, mult_let, mult_word, valid_placement):
    self.block = block
    self.occ = occ
    self.mult_let = mult_let
    self.mult_word = mult_word
    self.valid_placement = valid_placement

p1turn = True

scrabble_board = [
  [Tile(None, False, 1, 3, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 3, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 3, False)],
  [Tile(None, False, 1, 1, False), Tile(None, False, 1, 2, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 3, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 3, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 2, False), Tile(None, False, 1, 1, False)],
  [Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 2, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 2, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False)],
  [Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 2, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 2, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False)],
  [Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 2, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 2, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False)],
  [Tile(None, False, 1, 1, False), Tile(None, False, 3, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 3, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 3, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 3, 1, False), Tile(None, False, 1, 1, False)],
  [Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False)],
  [Tile(None, False, 1, 3, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, True), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 3, False)],
  [Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False)],
  [Tile(None, False, 1, 1, False), Tile(None, False, 3, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 3, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 3, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 3, 1, False), Tile(None, False, 1, 1, False)],
  [Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 2, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 2, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False)],
  [Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 2, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 2, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False)],
  [Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 2, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 2, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False)],
  [Tile(None, False, 1, 1, False), Tile(None, False, 1, 2, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 3, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 3, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 2, False), Tile(None, False, 1, 1, False)],
  [Tile(None, False, 1, 3, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 3, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 2, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 1, False), Tile(None, False, 1, 3, False)]
]  

block_bag = []
for i in range(97,123):
  let = chr(i).upper()
  if("AI".__contains__(let)):
    for i in range(0, 9):
      block_bag.append(Block(let))
  elif("NRT".__contains__(let)):
    for i in range(0, 6):
      block_bag.append(Block(let))
  elif("LSUD".__contains__(let)):
    for i in range(0, 4):
      block_bag.append(Block(let))
  elif("BCMPFHVWY".__contains__(let)):
    for i in range(0, 2):
      block_bag.append(Block(let))
  elif("KGXQZ".__contains__(let)):
    for i in range(0, 1):
      block_bag.append(Block(let))
  elif("G".__contains__(let)):
    for i in range(0, 3):
      block_bag.append(Block(let))
  elif("O".__contains__(let)):
    for i in range(0, 8):
      block_bag.append(Block(let))
  elif("E".__contains__(let)):
    for i in range(0, 12):
      block_bag.append(Block(let))
np.random.shuffle(block_bag)

  
def print_board():
  for i in range(0,15):
    for j in range(0,15):
      max = scrabble_board[i][j].mult_let
      if(scrabble_board[i][j].mult_let < scrabble_board[i][j].mult_word):
        max = scrabble_board[i][j].mult_word
      print(max, end="")
    print("")

def dic_search(word, min, max):
  file = open("Dic.txt")
  words = file.readlines()
  mid = (int)((min+max)/2)
  if(max >= min):
    if(words[mid] == word+"\n"):
      file.close()
      return True
    elif((words[mid]) > word):
      return dic_search(word, min, mid-1)
    else:
      return dic_search(word, mid+1, max)
  else:
    file.close()
    return False
  
def word_val_hor(i, j):
  word_mult_arr = []
  while(scrabble_board[i][j-1].occ == True and j > 0):
    j -= 1
  ret_val = scrabble_board[i][j].block.value*scrabble_board[i][j].mult_let #first block
  search_str = ""+scrabble_board[i][j].block.letter
  if(scrabble_board[i][j].mult_word > 1):
    word_mult_arr.append(scrabble_board[i][j].mult_word)
  if(j != 14):
    while(j < 14 and scrabble_board[i][j+1].occ == True):
      j += 1
      search_str += scrabble_board[i][j].block.letter
      ret_val += scrabble_board[i][j].block.value*scrabble_board[i][j].mult_let
      if(scrabble_board[i][j].mult_word > 1):
        word_mult_arr.append(scrabble_board[i][j].mult_word)
  if(dic_search(search_str, 0, 76353) == True):
    temp = ret_val #for mult word purposes incase there are multiple mult word multipliers
    for i in word_mult_arr:
      ret_val += i*temp
    if(temp != ret_val):
      ret_val -= temp #if word mult is applied temp != ret_val and ret_val will be too large(x2 will be x3 ect)
    return ret_val   
  return 0

def word_val_vert(i, j):
  word_mult_arr = []
  while(scrabble_board[i-1][j].occ == True and i > 0):
    i -= 1
  ret_val = scrabble_board[i][j].block.value*scrabble_board[i][j].mult_let
  search_str = ""+scrabble_board[i][j].block.letter
  if(scrabble_board[i][j].mult_word > 1):
    word_mult_arr.append(scrabble_board[i][j].mult_word)
  if(i != 14):
    while(i < 14 and scrabble_board[i+1][j].occ == True):
      i += 1
      search_str += scrabble_board[i][j].block.letter
      ret_val += scrabble_board[i][j].block.value*scrabble_board[i][j].mult_let
      if(scrabble_board[i][j].mult_word > 1):
        word_mult_arr.append(scrabble_board[i][j].mult_word)
  if(dic_search(search_str, 0, 76353) == True):
    temp = ret_val #for mult word purposes incase there are multiple mult word multipliers
    for i in word_mult_arr:
      ret_val += i*temp
    if(temp != ret_val):
      ret_val -= temp
    return ret_val   
  return 0

def place_block(block, i, j):
  if(scrabble_board[i][j].valid_placement):
    scrabble_board[i][j].block = block
    scrabble_board[i][j].occ = True
    score = word_val_hor(i, j) #move these methods to a new checker method that is called when button is pressed. remove the letters if score = 0 in method
    score += word_val_vert(i, j)
    if(i > 0):
      scrabble_board[i-1][j].valid_placement = True
    if(i < 14):
      scrabble_board[i+1][j].valid_placement = True
    if(j > 0):
      scrabble_board[i][j-1].valid_placement = True
    if(j < 14):
      scrabble_board[i][j+1].valid_placement = True
    return score
      
def reset_board():
  for i in range(0, 15):
    for j in range(0, 15):
      scrabble_board[i][j].valid_placement = False
      scrabble_board[i][j].block = None
      scrabble_board[i][j].occ = False
  scrabble_board[7][7].valid_placement = True
