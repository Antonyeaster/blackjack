# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time
import sys
import random
from time import sleep

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


def create_deck():
    """
    Creates a deck of 52 cards to be picked at random
    """
    return [
        2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K" "A",
        2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K" "A",
        2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K" "A",
        2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K" "A"
        ]  


deck = create_deck()



type_text("Welcome to BlackJack")

username = input("Whats your name? ")
print("Welcome", username, "lets have some fun")
