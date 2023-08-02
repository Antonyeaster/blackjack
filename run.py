# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time
import sys
import random
from time import sleep
from os import system, name


def type_text(text):
    """
    Creates typewriter effect for added expeirence
    """
    for i in text + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)


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


def game_rules():
    """
    To be displayed at the begining of the game,
    giving the user an option to read the rules.
    """
    while (True):

        type_text("Welcome to BlackJack")
        rules = str(
            input("Would you like to view the game rules? (y/n) ").lower())
        if rules == "y":
            clear()
            sleep(1)
            type_text("The aim of the game is to get 21")
            type_text("Or as close to 21 as possible without going over")
            type_text("To do this, you will be dealt 2 cards")
            type_text("The house will aslo be dealt 2 cards")
            type_text("All number cards are equivalent to the number on the card")
            type_text("Face cards (Jack, Queen, King) are all 10")
            type_text("Ace is the special card, it can be either 1 or 11")
            type_text("You can choose what you want ace to be\n")
            type_text("When you have your cards, you can choose to hit or stand")
            type_text("Hit will deal you another card to move closer to 21")
            type_text("Stand will confirm you are happy with the cards you have")
            type_text("and the house hand will be revealed")
            type_text("Who ever is closest to 21 wins")
            type_text("If you have 21, congrats, you have blackJack, you win")
            type_text("If the house hand has blackJack they win\n")
            type_text("Example cards dealt (K, 4) = 14, I could choose to hit")
            type_text("I will be dealt another card (k, 4, 6) now I have 20")
            type_text("Now I would choose to stand\n")

        elif rules == "n":
            type_text("Ok, sure! Lets get straight to it")

        else:
            type_text("Invalid option selected, select y/n ")
            continue

        while (True):
            
            start = str(
                input("Would you like to start the game? (y/n) ").lower())
            if start == "y":
                clear()
                type_text("Starting game....")
                sleep(2)
                clear()
            elif start == "n":
                type_text("Ok, see ya next time!")
                sleep(3)
                clear()
                quit()
            else:
                print("Invalid option selected, select y/n ")
                continue

    username = input("Whats your name? ")
    print("Welcome", username, "lets have some fun")

    return rules


play_by_the_rules = game_rules()


def main_blackjack():
    """
    Main game function to run a single game,
    with the option to play over and over
    """


main_blackjack()
