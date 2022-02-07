from data import data
import random
from os import system
from art import logo, vs


def format_data(account):
  """Format data into printable format"""
  account_name = account["name"]
  account_desc = account["description"]
  account_from = account["country"]
  return f"{account_name}, a {account_desc}, from {account_from}"


def check_answers(guess, followers_a, followers_b):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong."""
  if followers_a > followers_b:
    return guess == 'a'
  else:
    return guess == 'b'


def game():
  """Higher lower game"""
  print(logo)
  score = 0
  is_game_over = False
  account_a = random.choice(data)
  account_b = random.choice(data)


  while not is_game_over:
  #generate random people from data
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
      account_b = random.choice(data)
    
    #format data for printing
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    
    guess = input("Who has more followers? type 'a' or 'b': ").lower()
    #get follower value
    follower_account_a = account_a['follower_count']
    follower_account_b = account_b['follower_count']

    is_correct = check_answers(guess, follower_account_a, follower_account_b)
    
    system("clear")
    print(logo)
    
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score} ")
    else:
      is_game_over = True
      print(f"Sorry, that's wrong. Final score: {score}")

game()