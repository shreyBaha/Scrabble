import numpy as np
#create word code array ex of word code 9-7-9-6-9-5 perhaps 13 cuz mult not applide to other thing
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

word_code_arr = []

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
  
def word_val_hor(i, j, from_val_vert): #add boolean like in rubiks cub proj
  word_mult_arr = []
  count = 0
  while(scrabble_board[i][j-1].occ == True and j > 0):
    j -= 1
    count+=1
  ret_val = scrabble_board[i][j].block.value*scrabble_board[i][j].mult_let #first block
  search_str = ""+scrabble_board[i][j].block.letter
  vert_val = 0
  word_code = f"{i}-{j}-"
  if(not from_val_vert):
    vert_val = word_val_vert(i, j, True)
    if(vert_val == None):
      return None
  if(scrabble_board[i][j].mult_word > 1):
    word_mult_arr.append(scrabble_board[i][j].mult_word)
  if(j != 14):
    while(j < 14 and scrabble_board[i][j+1].occ == True):
      j += 1
      count+=1
      search_str += scrabble_board[i][j].block.letter
      ret_val += scrabble_board[i][j].block.value*scrabble_board[i][j].mult_let
      word_code += f"{i}-{j}-"
      if(not from_val_vert):
        new = word_val_vert(i, j, True)
        if(new == None):
          return None
        else:
          vert_val += new
      if(scrabble_board[i][j].mult_word > 1):
        word_mult_arr.append(scrabble_board[i][j].mult_word)
  if(dic_search(search_str, 0, 76353) == True and not (word_code in word_code_arr)):
    word_code_arr.append(word_code)
    temp = ret_val #for mult word purposes incase there are multiple mult word multipliers
    for i in word_mult_arr:
      ret_val += i*temp
    if(temp != ret_val):
      ret_val -= temp #if word mult is applied temp != ret_val and ret_val will be too large(x2 will be x3 ect)
    ret_val+=vert_val
    return ret_val
  elif((from_val_vert and count == 0) or (word_code in word_code_arr)):
    return 0
  #else if bool and count > 0 return None
  return None

def word_val_vert(i, j, from_val_hor):
  word_mult_arr = []
  count = 0
  while(scrabble_board[i-1][j].occ == True and i > 0):
    i -= 1
    count += 1
  ret_val = scrabble_board[i][j].block.value*scrabble_board[i][j].mult_let
  search_str = ""+scrabble_board[i][j].block.letter
  hor_val = 0
  word_code = f"{i}-{j}-"
  if(not from_val_hor):
    hor_val = word_val_hor(i, j, True)
    if(hor_val == None):
      return None
  if(scrabble_board[i][j].mult_word > 1):
    word_mult_arr.append(scrabble_board[i][j].mult_word)
  if(i != 14):
    while(i < 14 and scrabble_board[i+1][j].occ == True):
      i += 1
      count+=1
      search_str += scrabble_board[i][j].block.letter
      ret_val += scrabble_board[i][j].block.value*scrabble_board[i][j].mult_let
      word_code += f"{i}-{j}-"
      if(not from_val_hor):
        new = word_val_hor(i, j, True)
        if(new == None):
          return None
        else:
          hor_val += new
      if(scrabble_board[i][j].mult_word > 1):
        word_mult_arr.append(scrabble_board[i][j].mult_word)
  if(dic_search(search_str, 0, 76353) == True and not (word_code in word_code_arr)):
    word_code_arr.append(word_code)
    temp = ret_val #for mult word purposes incase there are multiple mult word multipliers
    for i in word_mult_arr:
      ret_val += i*temp
    if(temp != ret_val):
      ret_val -= temp
    ret_val+=hor_val
    return ret_val   
  elif((from_val_hor and count == 0) or (word_code in word_code_arr)):
    return 0
  return None

def get_score(i, j, word_hor):
  if(word_hor):
    score = word_val_hor(i, j, False)
  else:
    score = word_val_vert(i, j, False)
  return score

def place_block(block, i, j): #move score to seperate method
  if(scrabble_board[i][j].valid_placement):
    scrabble_board[i][j].block = block
    scrabble_board[i][j].occ = True
    #score = word_val_hor(i, j) #move these methods to a new checker method that is called when button is pressed. remove the letters if score = 0 in method
    #score += word_val_vert(i, j)
    if(i > 0):
      scrabble_board[i-1][j].valid_placement = True
    if(i < 14):
      scrabble_board[i+1][j].valid_placement = True
    if(j > 0):
      scrabble_board[i][j-1].valid_placement = True
    if(j < 14):
      scrabble_board[i][j+1].valid_placement = True
    #return score
      
def reset_board():
  for i in range(0, 15):
    for j in range(0, 15):
      scrabble_board[i][j].valid_placement = False
      scrabble_board[i][j].block = None
      scrabble_board[i][j].occ = False
  scrabble_board[7][7].valid_placement = True
