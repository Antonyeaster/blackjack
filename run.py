# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time
import sys
import random
from time import sleep
from os import system, name

class Deck:
    """
    Creates instances of the deck
    """
    def __init__(self):
        """
        
        """
        self.cards = []
        suits = ["Hearts", "Spade", "Diamonds", "Clubs"]
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10},        
        ]
        for suit in suits:
            for rank in ranks:
                self.cards.append([suit, rank])


class CardType:
    """
    Create instances for the different types of cards
    """
    def __init__(self, suit, rank):
        """
        
        """
        self.suit = suit
        self.rank = rank


def mix_up(self):
    """
    Shuffle all cards in the deck.
    """
    if len(self.card) > 1:
        random.shuffle(self.cards)


def dealt(num):
    """
    To select 2 cards from the deck and be dealt to 
    the player and computer.
    """
    cards_to_be_dealt = []
    for i in range(num):
        if len(self.card) > 0:
            card = self.cards.pop()
            cards_to_be_dealt.append(card)
    return cards_to_be_dealt


mix_up()
card = dealt(1)[0]
print(card[1]["value"])


def type_text(text):
    """
    Creates typewriter effect for added expeirence
    """

    for i in text + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(4)