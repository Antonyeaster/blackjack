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
        To be able to pull any suit or value from the deck and into
        the player or computers hand.
        """
        self.cards = []
        suits = ["Hearts", "Spade", "Diamonds", "Clubs"]
        card_values = [
            {"card_value": "A", "value": 11},
            {"card_value": "2", "value": 2},
            {"card_value": "3", "value": 3},
            {"card_value": "4", "value": 4},
            {"card_value": "5", "value": 5},
            {"card_value": "6", "value": 6},
            {"card_value": "7", "value": 7},
            {"card_value": "8", "value": 8},
            {"card_value": "9", "value": 9},
            {"card_value": "10", "value": 10},
            {"card_value": "J", "value": 10},
            {"card_value": "Q", "value": 10},
            {"card_value": "K", "value": 10},
        ]
        for suit in suits:
            for card_value in card_values:
                self.cards.append(CardType(suit, card_value))

    def mix_up(self):
        """
        Shuffle all cards in the deck.
        """
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def dealt(self, num):
        """
        To select 2 cards from the deck and be dealt to
        the player and computer.
        """
        cards_to_be_dealt = []
        for i in range(num):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_to_be_dealt.append(card)
        return cards_to_be_dealt


class CardType:
    """
    Create instances for the different types of cards
    """

    def __init__(self, suit, card_value):
        """
        To retrieve the suit and rank from the dictionary.
        """
        self.suit = suit
        self.card_value = card_value

    def __str__(self):
        """
        To return the string of the rank and suit.
        """
        return f"{self.card_value['card_value']} of {self.suit}"


class CardsInHand:
    def __init__(self, house_hand=False):
        """
        To create a hand for each player.
        """
        self.value = 0
        self.cards = []
        self.house = house_hand

    def new_card(self, card_list):
        """
        To retrieve a new card when you press hit.
        """
        self.cards.extend(card_list)


def type_text(text):
    """
    Creates typewriter effect for added expeirence
    """

    for i in text + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(4)


deck = Deck()
deck.mix_up()

hand = CardsInHand()
hand.new_card(deck.dealt(2))
print(hand.cards[0], hand.cards[1])
