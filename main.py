# Game Designed By Mahaveer

import random 
import time

rock = 1
paper = 2
scissors = 3

names = {rock: "Rock", paper: "Paper", scissors:"Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}

player_score = 0
computer_score = 0

def start():
  print("Let's Play The Game Of Rock, Paper and Scissors")
  game()

def game():
  player = move()
  computer = random.randrange(1, 3)
  result(player, computer)
  return play_again()

def move():
  while True:
    player = input("\nEnter Your Number\nFor Rock = 1\nFor Paper = 2\nFor scissors = 3\nFor GiveUp = 4\nMake a move: ")
    try:
      player = int(player)
      if player == 4:
        print("BYe BYe!")
        exit()
      if player in (1,2,3):
        return player
    except ValueError:
      pass
    print("Oops! I didn't understand. Please enter 1, 2 and 3.")

def result(player, computer):
  print("\nComputer Is Thinking")
  print("3...")
  time.sleep(0.5)
  print("2..")
  time.sleep(0.5)
  print("1.")
  time.sleep(0.5)

  print("Computer Threw {0}!".format(names[computer]))

  global player_score, computer_score
  if player == computer:
    print("Game Tie")
  else:
    if rules[player] == computer:
      print("Your victory has been assured")
      player_score = player_score + 1
    else:
      print("Computer laughed as you realized you have been defeated")
      computer_score = computer_score + 1
    print("\nThe Total Score")
    print("Player:", player_score)
    print("Computer:", computer_score)

def play_again():
  answer = input("\nWould you like to Play Again? Yes/No: ")
  if answer in ("y","Y","yes","Yes","Of course!"):
    return start()
  else:
    print("Thankyou so much for playing! We will see you in next time")

if __name__ == "__main__":
  start()

