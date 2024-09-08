#WORDLE CODE:

from spellchecker import SpellChecker

spell = SpellChecker()
def check(word):
  if word == spell.correction(word):
    return True
  else:
    return False
import os

import time
#from replit import audio
from PyDictionary import PyDictionary
dict = PyDictionary()
player_1_score = 0
player_2_score = 0
guess_list = []



import random
words_list = [
   "apple", "grape", "lemon", "bread", "water", "piano", "music", "money",
"paper", "brush", "pound", "sugar", "sweet", "heart", "laugh", "light", "green", "white",
"black", "brown", "happy", "smile", "write", "learn", "study", "party", "watch", "movie",
"sound", "quiet", "speak", "voice", "early", "later", "never", "always", "fruit", "plant",
"field", "beach", "ocean", "river", "earth", "world",
"train", "plane", "hotel", "store", "cream", "sugar", "spoon", "knife", "plate",
"glass", "cloth", "shirt", "pants", "shoes", "socks", "watch", "chain", "brace", "glove",
"photo", "frame", "paint", "brush", "color", "wheel", "cycle", "motor", "power", "light",
"phone", "cable", "mouse", "floor", "wall",
"metal", "steel", "paper", "cloth", "silk", "badge", "beach", "bloom", "blush", "booth", "braid", "bread", "break", "broom", "brush",
"cabin", "cable", "chair", "charm", "chase", "cheek", "chill", "choir", "clasp",
"cloud", "coach", "couch", "creek", "crowd", "crown", "crush", "curve",
"dance", "daisy", "delta", "diner", "ditch", "diver", "dough", "draft",
"drama", "dream", "dress", "drill", "drink", "drive", "dwarf", "eagle", "earth", "elbow",
"email", "equal", "error", "event", "exile", "extra", "fable", "faith", "feast", "field",
"flame", "flock", "flour", "fluid", "frame", "frost", "fruit", "giant", "glass", "globe",
"glove", "grace", "grain", "grand", "grape", "grass", "grief", "group", "guard", "guest",
"guide", "habit", "haste", "hatch", "heart", "hobby", "honor", "horse", "hotel", "house",
"humor", "index", "input", "issue", "jeans", "jelly", "jewel", "joint", "juice", "jumbo",
"kneel", "knife", "knock", "label", "laugh", "lemon", "light", "limit", "liver", "lunch",
"magic", "major", "mango", "maple", "march", "match", "medal", "melon", "merit", "meter",
"might", "minor", "mixer", "money", "movie", "music", "noble", "noise", "novel", "ocean",
"olive", "onion", "opera", "orbit", "order", "otter", "paint", "panda", "panel", "paper",
"party", "pasta", "patio", "peach", "pearl", "piano", "pilot", "pizza", "place", "plant",
"plate", "plaza", "plume", "polar", "power", "pride", "print", "prize", "punch", "puppy",
"quart", "queen", "quote", "radio", "rainy", "rally", "raven", "razor", "react", "realm",
"rebel", "ridge", "rival", "river", "roast", "robot", "rough", "round", "royal", "rural",
"satin", "scale", "scene", "scent", "score", "scout", "shark", "sheep", "shelf", "shine",
"shirt", "shock", "shout", "skate", "skill", "skirt", "skull", "slate", "sloth", "smile",
"snack", "snake", "sneak", "speak", "spice", "spike", "sport", "squad", "stage", "stake",
"stall", "stamp", "stand", "stare", "steak", "steel", "stick", "stone", "stool", "store",
"storm", "story", "stove", "straw", "strip", "study", "style", "sugar", "sunny", "sweat",
"sweep", "swim", "swing", "table", "taste", "teach", "teeth", "theme", "thief", "thumb",
"tiger", "toast", "today", "topic", "torch", "tower", "trade", "train", "treat", "trick",
"trunk", "tulip", "tutor", "twist", "unity", "upper", "urban", "usage", "vapor", "vegan",
"velvet", "virus", "vocal", "voice", "voter", "waste", "water", "whale", "wheat", "wheel",
"whisk", "white", "whole", "woman", "world", "worry", "worth", "wound", "woven", "zebra"
]



current_list = []
check_current_list = []
current_word = ""
wordle_score = 0
gameLoop = True
while gameLoop:
  word = random.choice(words_list)

  game_choice = input("What game would you like to play Tic Tac Toe(2-PLAYER) [T] or Wordle(1-PLAYER) [W] or Quit [Q]?: ")

  if game_choice.lower() in ['w','wordle', 'wo', 'wor', 'word', 'wordl']:
    start_time = time.time()
    wordle = list(word.strip())
    globalLoop = True
    os.system('clear')
    print("="*183)
    print('\033[01m' "Welcome to Wordle!" '\033[0m')
    print("="*183)
    print("\n")
    print("To play, you will be allowed to guess 5 letter words. You're goal is to guess a randomly chosen 5 letter word. When guessing, letters that are in the correct position and in target will be highlighted in green. Letters that are in the target word but in the incorrect position will be highlighted in yellow. Any letter left gray means it is not in the target word. Good luck!! ")
    print("\n")
    print("If you guess the correct word in 6 guesses or less, you will receive 10 points. If you guess in between 6 and 10 guesses, you will receive 3 points. If you guess more than 10 guesses, you don't receive any points! :( ")
    print("\n")
    
    while globalLoop:
      guess_list = []
      decision = input("Do you want to play? Y/N: ")
      counter = 0
      if decision.lower() in ['y', 'yes','ye','sure','yup','of course', 'absolutely','yuh','yur']:
        guessLoop = True
        print("Please enter a five letter word guess! _ _ _ _ _: ")
        
        
        while guessLoop:
          if check_current_list == wordle:
            end_time = time.time()
            time_passed = int(end_time - start_time)

            meaning = str(dict.meaning(word))
            #source = audio.play_file("street-fighter-ii-you-win-perfect.mp3")
            print("\n")
            print("="*183)
            print(f"The definition of \033[01m{word:s}\033[0m is: \n {meaning:s}.")
            print("="*183)
            print("\n")
            print('\033[01m'"YOU WIN!"'\033[0m')
            print('\033[01m'f"That took you {counter:d} guesses!"'\033[0m')
            print(f"That Wordle took you {time_passed:d} seconds!")
            if counter <= 6:
              wordle_score += 10
            elif 6 < counter <= 10:
              wordle_score += 3
            else:
              wordle_score += 0
            print(f"You now have {wordle_score:d} points!")
            print("\n")
            
            guessLoop = False
            globalLoop = False
            current_list = []
            current_word = ""
            check_current_list = []
            guess_list = []
            break
          current_list = []
          current_word = ""
          check_current_list = []
          guess = input("")
          if check(guess):
            if len(guess) == 5 and guess.isalpha():
              if not guess.lower() in guess_list:
                guess_list.append(guess.lower())
                guess_strip = list(guess.strip())
                index = 0 
                counter += 1
                for letter in guess:
                  if wordle[index].lower() == guess_strip[index].lower():
                    current_list.append("\033[1;32m" + guess_strip[index].upper() + "\033[0m")
                    check_current_list.append(guess_strip[index].lower())
                    index += 1
                  elif guess_strip[index].lower() in wordle:
                    current_list.append('\33[33m' + guess_strip[index].upper() + '\033[0m')
                    check_current_list.append(guess_strip[index].lower())
                    index += 1
                  else:
                    current_list.append(guess_strip[index].upper())
                    check_current_list.append(guess_strip[index].lower())
                    index += 1
              else:
                print("You already guessed that word!")
          
            else:
              print("Please enter a valid five letter word guess")
          else:
            print("Please enter a real English word!")
    
          current_word = current_word.join(current_list)
          print(current_word)
      elif decision.lower() in ['no','n']:
        print("Thanks for playing!")
        globalLoop = False
        break
      else:
        print("Please enter a valid answer") 
#TIC TAC TOE CODE:  
  elif game_choice.lower() in ['t','tic tac toe','ttt','tictactoe','tic','tic tac']:
    

    
    import random
    
    player_1 = "X"
    player_2 = "O"
    players = ["X","O"]
    

    
    board = [
    ['[ ]','[ ]','[ ]'],
    ['[ ]','[ ]','[ ]'],
    ['[ ]','[ ]','[ ]']
    ]
    
    
    def board_print():
      for row in board:
        print(''.join(row))
    
    
    index = random.randint(0,1)
    piece = players[index]
    
    guessLoop2 = True
    globalLoop2 = True
    guesses = 0
    while globalLoop2:
      board = [
    ['[ ]','[ ]','[ ]'],
    ['[ ]','[ ]','[ ]'],
    ['[ ]','[ ]','[ ]']
    ]
      os.system('clear')
      print('\033[01m' "Tic Tac Toe Board To Follow:" '\033[0m')
      print('''
    [ 1 ][ 2 ][ 3 ]
    [ 4 ][ 5 ][ 6 ]
    [ 7 ][ 8 ][ 9 ]
    '''
    )
      
      print('\033[01m' "Welcome to Tic Tac Toe!"'\033[0m')
      print("This game requires two players, go grab a friend!")
      
      board_print()
        
      guessLoop2 = True
      
    
      while guessLoop2:
        if (board[0][0] == board[0][1] == board[0][2] != '[ ]'or
            board[1][0] == board[1][1] == board[1][2] != '[ ]' or
            board[2][0] == board[2][1] == board[2][2] != '[ ]' or
            board[0][0] == board[1][0] == board[2][0] != '[ ]' or
            board[0][1] == board[1][1] == board[2][1] != '[ ]' or
            board[0][2] == board[1][2] == board[2][2] != '[ ]' or
            board[0][0] == board[1][1] == board[2][2] != '[ ]' or
            board[0][2] == board[1][1] == board[2][0] != '[ ]'):
          
          if piece == "X":
            print(f"Player {piece:s} has won!")
            player_1_score += 1
            print("\n")
          elif piece == "O":
            print(f"Player {piece:s} has won!")
            player_2_score += 1
            print("\n")
          
          print('\033[01m' f"The score is X: {player_1_score:d} to O: {player_2_score:d}" '\033[0m')
          print("\n")
          guessLoop2 = False
          globalLoop2 = False
          
          break
          
        elif guesses >= 9:
          print("Nobody wins!")
          print("\n")
          guessLoop2 = False
          globalLoop2 = False
          
          break
        else:
          try:
            piece = players[index]
            guesses += 1
            move = int(input(f"Where does player {piece:s} want to place? (Please respond 1-9): "))
            
      
            if move == 1 and board[0][0] == '[ ]':
              if piece == "X":
                board[0][0] = f"[\033[94m{piece}\033[0m]"
              elif piece == "O":
                board[0][0] = f"[\033[31m{piece}\033[00m]"
              if index == 1:
                index = index - 1
              elif index == 0:
                index = index + 1
                
            elif move == 2 and board[0][1] == '[ ]':
              if piece == "X":
                board[0][1] = f"[\033[94m{piece}\033[0m]"
              elif piece == "O":
                board[0][1] = f"[\033[31m{piece}\033[00m]"
              if index == 1:
                index = index - 1
              elif index == 0:
                index = index + 1
                
            elif move == 3 and board[0][2] == '[ ]':
              if piece == "X":
                board[0][2] = f"[\033[94m{piece}\033[0m]"
              elif piece == "O":
                board[0][2] = f"[\033[31m{piece}\033[00m]"
              if index == 1:
                index = index - 1
              elif index == 0:
                index = index + 1
                
            elif move == 4 and board[1][0] == '[ ]':
              if piece == "X":
                board[1][0] = f"[\033[94m{piece}\033[0m]"
              elif piece == "O":
                board[1][0] = f"[\033[31m{piece}\033[00m]"
              if index == 1:
                index = index - 1
              elif index == 0:
                index = index + 1
                
            elif move == 5 and board[1][1] == '[ ]':
              if piece == "X":
                board[1][1] = f"[\033[94m{piece}\033[0m]"
              elif piece == "O":
                board[1][1] = f"[\033[31m{piece}\033[00m]"
              if index == 1:
                index = index - 1
              elif index == 0:
                index = index + 1
                
            elif move == 6 and board[1][2] == '[ ]':
              if piece == "X":
                board[1][2] = f"[\033[94m{piece}\033[0m]"
              elif piece == "O":
                board[1][2] = f"[\033[31m{piece}\033[00m]"
              if index == 1:
                index = index - 1
              elif index == 0:
                index = index + 1
                
            elif move == 7 and board[2][0] == '[ ]':
              if piece == "X":
                board[2][0] = f"[\033[94m{piece}\033[0m]"
              elif piece == "O":
                board[2][0] = f"[\033[31m{piece}\033[00m]"
              if index == 1:
                index = index - 1
              elif index == 0:
                index = index + 1
                
            elif move == 8 and board[2][1] == '[ ]':
              if piece == "X":
                board[2][1] = f"[\033[94m{piece}\033[0m]"
              elif piece == "O":
                board[2][1] = f"[\033[31m{piece}\033[00m]"
              if index == 1:
                index = index - 1
              elif index == 0:
                index = index + 1
                
            elif move == 9 and board[2][2] == '[ ]':
              if piece == "X":
                board[2][2] = f"[\033[94m{piece}\033[0m]"
              elif piece == "O":
                board[2][2] = f"[\033[31m{piece}\033[00m]"
              if index == 1:
                index = index - 1
              elif index == 0:
                index = index + 1
          
            else:
              print("Please enter a value between 1 and 9 on the board that has not been filled in yet: ")
              guesses -= 1
          except ValueError:
            print("Please enter a value between 1 and 9 on the board that has not been filled in yet: ")
            guesses -= 1

          os.system('clear')
          print('\033[01m' "Tic Tac Toe Board To Follow:" '\033[0m')
          print('''
    [ 1 ][ 2 ][ 3 ]
    [ 4 ][ 5 ][ 6 ]
    [ 7 ][ 8 ][ 9 ]
    '''
    )
          print("\n")
          print("Updated Board: ")
          for row in board:
            print(''.join(row))
  elif game_choice.lower() in ['quit','q','qu','qui','bye','no','none','nah','absolutely not']:
    gameLoop = False
    globalLoop = False
    guessLoop = False
    guessLoop2 = False
    globalLoop2 = False
    os.system('clear')
    break
    
    
  else:
    print("Please choose one of the provided options!")
