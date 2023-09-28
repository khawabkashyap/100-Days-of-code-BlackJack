import os
import random

from getkey import getkey, keys

if os.name == 'nt':
  # Windows
  def Clear():
    return os.system('cls')
else:
  # other mainly Linux or Unix base OS
  def Clear():
    return os.system('clear')
  
class Card:
  def __init__(self, value, symbol, suit):
    self.value = value
    self.symbol = symbol
    self.suit = suit

  def __str__(self):
    return self.symbol + self.suit

logo = """
\x1b[42m\x1b[30m.------.            _     _            _    _            _    
|A_  _ |           | |   | |          | |  (_)          | |   
|( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  /|K /\\  |     | '_ \\| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
      |  \\/ K|                            _/ |                
      `------'                           |__/                 \x1b[0m\n"""

def AskContinue():
  print("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  answer = getkey()
  answer = answer.lower()
  if answer[0] == 'y':
    return True
  return False

def AskForCard():
  print("Type 'y' to get another card, type 'n' to pass: ")
  answer = getkey()
  answer = answer.lower()
  if answer[0] == 'y' or answer[0] == 'h':
    return True
  return False

def DealCard():
  deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]
  suits = ["♠", "♥", "♣", "♦"]
  value = random.choice(deck)
  if value == 11:
    symbol = "A"
  elif value == 12:
    value = 10
    symbol = "J"
  elif value == 13:
    value = 10
    symbol = "Q"
  elif value == 14:
    value = 10
    symbol = "K"
  else:
    symbol = str(value)
  suit = random.choice(suits)
  NewCard = Card(value, symbol, suit)
  return NewCard

def firstDeal():
  NewCards = []
  for _ in range(2):
    NewCards.append(DealCard())
  return NewCards

def SumCards(Hand):
  result = 0
  for card in Hand:
    result += card.value
  return result

def Ace11to1(Hand):#check for errors
  for card in Hand:
    if card.value == 11:
      card.value = 1
      check = SumCards(Hand)
      if check < 22:
        break
  return Hand

def ShowCard(card):
  if (card.suit == "♠") or (card.suit == "♣"):
    print("\u001b[47m\u001b[30m", end = "")
  else:
    print("\u001b[47m\u001b[31m", end = "")
  print(card, end = "")
  print("\u001b[0m", end = "")

def ShowHand(Hand, Score, who):
  if who == "player":
    print("   Your cards: ", end = "")
  else:
    print("   Computer's final cards: ", end = "")
  for card in Hand:
    ShowCard(card)
    print(" ", end = "")
  print(f"with a score of: {Score}")

ContinuePlaying = AskContinue()
while ContinuePlaying:
  Clear()
  print(logo)
  PlayerCards = firstDeal()
  PlayerScore = SumCards(PlayerCards)
  if PlayerScore > 21:
    PlayerCards = Ace11to1(PlayerCards)
    PlayerScore = SumCards(PlayerCards)
  ShowHand(PlayerCards, PlayerScore, "player")
  ComputerCards = firstDeal()
  ComputerScore = SumCards(ComputerCards)
  if ComputerScore > 21:
    ComputerCards = Ace11to1(ComputerCards)
    ComputerScore = SumCards(ComputerCards)
  print("   Computer's first card: ", end = "")
  ShowCard(ComputerCards[0])
  print("")
  HitMe = False if PlayerScore == 21 else AskForCard()
  while HitMe:
    NewCard = DealCard()
    PlayerCards.append(NewCard)
    PlayerScore = SumCards(PlayerCards)
    if PlayerScore > 21:
      PlayerCards = Ace11to1(PlayerCards)
      PlayerScore = SumCards(PlayerCards)
      ShowHand(PlayerCards, PlayerScore, "player")
      if PlayerScore == 21:
        HitMe = False
      else:
        HitMe = False if PlayerScore > 21 else AskForCard()
    elif PlayerScore == 21:
      ShowHand(PlayerCards, PlayerScore, "player")
      HitMe = False
    else:
      ShowHand(PlayerCards, PlayerScore, "player")
      HitMe = AskForCard()
  while ComputerScore < 17:
    NewCard = DealCard()
    ComputerCards.append(NewCard)
    ComputerScore = SumCards(ComputerCards)
    if ComputerScore > 21:
      ComputerCards = Ace11to1(ComputerCards)
      ComputerScore = SumCards(ComputerCards)
  ShowHand(ComputerCards, ComputerScore, "computer")
  if PlayerScore > 21:
    print("\nLoose, you bust for being over 21 points \U0001F622\n")
  elif ComputerScore == 21:
    print("\nLoose, the computer has Blackjack \U0001F61F\n")
  elif PlayerScore == 21:
    print("\nWin, you have Blackjack and the computer doesn't \U0001F973\n")
  elif ComputerScore > 21:
    print("\nWin, the computer bust but you did't \U0001F60A\n")
  elif PlayerScore == ComputerScore:
    print("\nIt's a tie \U0001FAE4\n")
  elif ComputerScore > PlayerScore:
    print("\nLoose, the computer has more points than you \U00002639\n")
  else:
    print("\nWin, you have more points than the computer \U0001F604\n")
  ContinuePlaying = AskContinue()

print("\nThank you for playing")