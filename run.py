# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time
import sys
import random
from time import sleep
from os import system, name

print("""
 _______   __                      __           _____                      __       
/       \ /  |                    /  |         /     |                    /  |      
$$$$$$$  |$$ |  ______    _______ $$ |   __    $$$$$ |  ______    _______ $$ |   __ 
$$ |__$$ |$$ | /      \  /       |$$ |  /  |      $$ | /      \  /       |$$ |  /  |
$$    $$< $$ | $$$$$$  |/$$$$$$$/ $$ |_/$$/  __   $$ | $$$$$$  |/$$$$$$$/ $$ |_/$$/ 
$$$$$$$  |$$ | /    $$ |$$ |      $$   $$<  /  |  $$ | /    $$ |$$ |      $$   $$<  
$$ |__$$ |$$ |/$$$$$$$ |$$ \_____ $$$$$$  \ $$ \__$$ |/$$$$$$$ |$$ \_____ $$$$$$  \ 
$$    $$/ $$ |$$    $$ |$$       |$$ | $$  |$$    $$/ $$    $$ |$$       |$$ | $$  |
$$$$$$$/  $$/  $$$$$$$/  $$$$$$$/ $$/   $$/  $$$$$$/   $$$$$$$/  $$$$$$$/ $$/   $$/
""")


def type_text(text):
    """
    Creates typewriter effect for added expeirence
    """
    for i in text + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.08)


def get_deck():
    """
    Creates a deck of 52 cards to be picked at random
    """
    return [
        2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A",
        2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A",
        2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A",
        2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]


deck = get_deck()


def clear():
    """
    This function will run to clear the terminal.
    """
    # Used information from https://www.geeksforgeeks.org/clear-screen-python/
    # Windows
    if name == "nt":
        _ = system("cls")
    # Mac and Linux
    else:
        _ = system("clear")


def get_hand():
    """
    Prepares for a new game by emptying hands
    """
    return []

    user_hand = get_hand()
    house_hand = get_hand()


def dealing_random_cards(hand):
    """
    Deals a random card from the deck and removes
    the card from the deck
    """
    dealt = random.choice(deck)
    hand.append(dealt)
    deck.remove(dealt)


def total_hand(hand):
    """
    Calculates cards in the deck which will
    help the user decide their next move
    """
    total = 0
    face_cards = ["K", "Q", "J"]
    for dealt in hand:
        if dealt in range(1, 11):
            total += dealt
        elif dealt in face_cards:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 10
    return total


def main_blackjack():
    """
    Main game function to run a single game, 
    with the option to play over and over
    """


    user_score = 0
    house_score = 0

    user_cards = []
    house_cards = []


main_blackjack()


type_text("Welcome to BlackJack")

username = input("Whats your name? ")
print("Welcome", username, "lets have some fun")
