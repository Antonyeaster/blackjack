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

    def __repr__(self):
        return f"CardType('{self.suit}', '{self.card_value}')"


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

    def get_hand_value(self):
        """
        Get the value of the hand to inform the player.
        """
        self.value = 0
        ace_included = False
               
        for card in self.cards:
            card_amount = int(card.card_value["value"])
            self.value += card_amount
            if card.card_value["card_value"] == "A":
                ace_included = True

        if ace_included and self.value > 21:
            self.value -= 10

    def total(self):
        """
        Return the total value in the hand.
        """
        self.get_hand_value()
        return self.value

    def equals_blackjack(self):
        """
        To establish if 21 has been achieved and blackjack happens
        """
        return self.total() == 21

    def display_hands(self, show_hidden_cards=False):
        """
        Display the players hand and the house hand.
        """
        print(f'''{"house's" if self.house else "Your"} hand: ''')
        for index, card in enumerate(self.cards):
            if index == 1 and self.house and not show_hidden_cards and not \
                    self.equals_blackjack():
                print("X")
            else:
                print(card)

        if not self.house:
            print("value:", self.total())
        print()


def type_text(text):
    """
    Creates typewriter effect for added expeirence
    """

    for i in text + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)


class PlayGame:

    def games(self):
        """
        To run the main game in a loop until player chooses to stop.
        """
        amount_of_games = 0
        game_number = 0

        while amount_of_games <= 0:
            try:
                amount_of_games = int(input(
                    "How many games would you like to play? "))
            except ValueError:
                print("Thats not a number, please try again")

        while game_number < amount_of_games:
            game_number += 1

            deck = Deck()
            deck.mix_up()
            player_hand = CardsInHand()
            house_hand = CardsInHand(house_hand=True)

            for i in range(2):
                player_hand.new_card(deck.dealt(1))
                house_hand.new_card(deck.dealt(1))

            print()
            print("-" * 40)
            print(f"You are on game {game_number} of {amount_of_games}")
            print("-" * 40)
            player_hand.display_hands()
            house_hand.display_hands()

            if self.who_wins(player_hand, house_hand):
                continue

            decision = ""
            while player_hand.total() < 21 and decision not in ["s", "stand"]:
                decision = input("Would you like to Hit or Stand:").lower()
                print()
                while decision not in ["hit", "stand", "h", "s"]:
                    decision = input("Options available are Hit or Stand or (h/s)").lower()
                    print()
                if decision in ["hit", "h"]:
                    player_hand.new_card(deck.dealt(1))
                    player_hand.display_hands()

            if self.who_wins(player_hand, house_hand):
                continue

            player_hand_amount = player_hand.total()
            house_hand_amount = house_hand.total()

            while house_hand_amount < 17:
                house_hand.new_card(deck.dealt(1))
                house_hand_amount = house_hand.total()

            house_hand.display_hands(show_hidden_cards=True)

            if self.who_wins(player_hand, house_hand):
                continue

            type_text("That's the end of the game, the final results are...")
            print("Your hand is:", player_hand_amount)
            print("House hand is:", house_hand_amount)

            self.who_wins(player_hand, house_hand, True)
            
    def who_wins(self, player_hand, house_hand, game_over=False):
        """
        To check the winner against various different outcomes.
        """
        if not game_over:
            if player_hand.total() > 21:
                print("Oops! You've bust! The House wins this round.")
                return True
            elif house_hand.total() > 21:
                print("The House has gone bust! You win this round.")
                return True
            elif house_hand.equals_blackjack():
                print("The House has Blackjack, They win, better luck next time")
                return True
            elif player_hand.equals_blackjack():
                print("WOW, you've got Blackjack, you win")
                return True
            elif player_hand.equals_blackjack() and house_hand.equals_blackjack():
                print("Shame, that was close but it's a draw this time")
                return True
        else:
            if house_hand.total() > player_hand.total():
                print("The House wins this round!")
            elif house_hand.total() == player_hand.total():
                print("It's a draw")
            else:
                print("Great job, you win!")
            return True
        return False


def welcome():
    type_text("Welcome to Blackjack")
    type_text("Lets take some time to get to know eachother")
    username = input("Whats your name? ")
    type_text(f"Hi {username} my names Jack, nice to meet you")


def game_rules():
    rules = str(input(f"So 'username' would you like to read the rules? yes or no ")).lower()
    if rules == "y":
        type_text("The rules are simple, hit 21")
    else:
        type_text("Ok, lets get straight to it!")


welcome()
game_rules()
go = PlayGame()
go.games()