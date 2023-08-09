# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time
import sys
import random
from time import sleep
from os import system, name

print("""
.------.------.------.------.------.
|B.--. |L.--. |A.--. |C.--. |K.--. |
| :(): | :/\: | (\/) | :/\: | :/\: |
| ()() | (__) | :\/: | :\/: | :\/: |
| '--'B| '--'L| '--'A| '--'C| '--'K|
`------`------`------`------`------'
.------.------.------.------.       
|J.--. |A.--. |C.--. |K.--. |      
| :(): | (\/) | :/\: | :/\: |      
| ()() | :\/: | :\/: | :\/: |      
| '--'J| '--'A| '--'C| '--'K|     
`------`------`------`------'
""")


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
        suits = ["Hearts \U00002665", "Spades \U00002660",
                 "Diamonds \U00002666", "Clubs \U00002663"]
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
        time.sleep(0.01)


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
                clear()
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
            print("\U00002665 \U00002660 \U00002666 \U00002663 " * 5)
            print()
            print(f"You are on game {game_number} of {amount_of_games}")
            print()
            print("\U00002665 \U00002660 \U00002666 \U00002663 " * 5)
            print()
            player_hand.display_hands()
            house_hand.display_hands()

            if self.who_wins(player_hand, house_hand):
                continue

            decision = ""
            while player_hand.total() < 21 and decision not in ["s", "stand"]:
                decision = input("Would you like to Hit or Stand:").lower()
                print()
                while decision not in ["hit", "stand", "h", "s"]:
                    decision = input(
                        "Options available are Hit or Stand or (h/s)").lower()
                    print()
                if decision in ["hit", "h"]:
                    player_hand.new_card(deck.dealt(1))
                    player_hand.display_hands()

            if self.who_wins(player_hand, house_hand):
                continue

            house_hand_amount = house_hand.total()

            while house_hand_amount < 17:
                house_hand.new_card(deck.dealt(1))
                house_hand_amount = house_hand.total()

            house_hand.display_hands(show_hidden_cards=True)

            if self.who_wins(player_hand, house_hand):
                continue

            self.who_wins(player_hand, house_hand, True)

    def who_wins(self, player_hand, house_hand, game_over=False):
        """
        To check the winner against various different outcomes.
        """
        player_hand_amount = player_hand.total()
        house_hand_amount = house_hand.total()

        if not game_over:
            if player_hand.total() > 21:
                type_text("Oops! You've bust! The House wins this round.")
                print("Your hand was:", player_hand_amount)
                print("House hand was:", house_hand_amount)
                print()
                sleep(4)
                return True
            elif house_hand.total() > 21:
                type_text("The House has gone bust! You win this round.")
                print("Your hand was:", player_hand_amount)
                print("House hand was:", house_hand_amount)
                print()
                sleep(4)
                return True
            elif house_hand.equals_blackjack():
                type_text(
                    "The House has Blackjack, They win, better luck next time")
                print("Your hand was:", player_hand_amount)
                print("House hand was:", house_hand_amount)
                print()
                sleep(4)
                return True
            elif player_hand.equals_blackjack():
                type_text("WOW, you've got Blackjack, you win")
                print("Your hand was:", player_hand_amount)
                print("House hand was:", house_hand_amount)
                print()
                sleep(4)
                return True
            elif player_hand.equals_blackjack() and house_hand.equals_blackjack():
                type_text("Shame, that was close but it's a draw this time")
                print()
                sleep(4)
                return True
        else:
            if house_hand.total() > player_hand.total():
                type_text("The House wins this round!")
                print("Your hand was:", player_hand_amount)
                print("House hand was:", house_hand_amount)
                print()
                sleep(4)
            elif house_hand.total() == player_hand.total():
                type_text("It's a draw")
                print("Your hand was:", player_hand_amount)
                print("House hand was:", house_hand_amount)
                print()
                sleep(4)
            else:
                type_text("Great job, you win!")
                print("Your hand was:", player_hand_amount)
                print("House hand was:", house_hand_amount)
                print()
                sleep(4)
            return True
        return False


def welcome():
    """
    A few typed out lines to welcome the user
    and retrieve their name.
    """
    type_text("Welcome to Blackjack")
    type_text("Lets take some time to get to know eachother \U0001F4A5")
    name = input("Whats your name? ")
    sleep(0.5)
    clear()
    type_text(f"Hi {name} my names Jack, nice to meet you")
    type_text(f"So {name}, would you like to read the rules?")


def game_rules():
    """
    To give the user the chance to read the rules
    or just go straight into the game.
    """
    read_rules = str(input("Y for yes or N for no? ")).lower()
    if read_rules == "y":
        type_text("The rules are simple, hit 21")
    elif read_rules == "n":
        clear()
        type_text("Ok, lets get straight to it!")
    else:
        type_text("Please enter Y or N ")


def play_again():
    """
    To give the user a chance to play agian.
    """
    re_run = True
    while re_run:
        type_text("Would you like to play again? (Y/N)")
        go_again = str(input("")).lower()

        if go_again == "y":
            clear()
            type_text("Awesome, new game loading....")
            sleep(2)
            run.games()
        elif go_again == "n":
            type_text("Well it was nice to meet you, thanks for playing.")
            exit()
        else:
            type_text("Please enter Y for yes or N for n")
            continue


def clear():
    """
    To clear the terminal for a more focused approach.
    """
    # For a Windows os
    if name == "nt":
        _ = system("cls")
    # For a Mac os
    else:
        _ = system("clear")


welcome()
game_rules()
run = PlayGame()
run.games()
play_again()
