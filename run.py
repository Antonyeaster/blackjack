# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time
import sys
import random
from time import sleep
from os import system, name

cards = []
suits = ["Hearts", "Spade", "Diamonds", "Clubs"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
for suit in suits:
    for rank in ranks:
        cards.append([suit, rank])


def mix_up():
    """
    Shuffle all cards in the deck.
    """
    random.shuffle(cards)


def dealt(num):
    """
    To select 2 cards from the deck and be dealt to 
    the player and computer.
    """
    cards_to_be_dealt = []
    for i in range(num):
        card = cards.pop()
        cards_to_be_dealt.append(card)
    return cards_to_be_dealt


mix_up()
cards_to_be_dealt = dealt(2)
card = cards_to_be_dealt[0]
number_or_face_card = card[1]

if number_or_face_card == "A":
    value = 11
print(cards_to_be_dealt)


def type_text(text):
    """
    Creates typewriter effect for added expeirence
    """

    for i in text + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)