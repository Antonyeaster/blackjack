# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time
import sys
import random
from time import sleep
from os import system, name

print(r"""
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
        for _ in range(num):
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
        print(f'''{"House" if self.house else player_name}'s hand: ''')
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
        time.sleep(0.04)


class PlayGame:

    def games(self):
        """
        To give the player a choice of how many games to play,
        and increase the game number by 1 when check winner has run.
        """
        amount_of_games = 0
        game_number = 0

        while amount_of_games <= 0:
            try:
                amount_of_games = int(input(
                    "How many games would you like to play?\n"))
                clear()
            except ValueError:
                print("Thats not a number, please try again")

        while game_number < amount_of_games:
            game_number += 1

            deck = Deck()
            deck.mix_up()
            player_hand = CardsInHand()
            house_hand = CardsInHand(house_hand=True)

            for _ in range(2):
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

            # Player decision options, runs if value is less then 21

            decision = ""
            while player_hand.total() < 21 and decision not in ["s", "stand"]:
                decision = input(
                    "Would you like to Hit, Stand or Quit:\n").lower()
                print()
                while decision not in ["hit", "stand", "h", "s", "quit", "q"]:
                    decision = input(
                        "Options available are Hit, Stand or Quit or "
                        "(h/s/q)\n(Letter casing does not matter)\n").lower()
                    print()
                if decision in ["hit", "h"]:
                    player_hand.new_card(deck.dealt(1))
                    player_hand.display_hands()
                if decision in ["quit", "q"]:
                    while True:
                        exit_game = str(input(
                            "Are you sure you want to quit? (Y/N)\n"))
                        if exit_game == "y":
                            type_text(
                                "\nOk, thanks for playing, come back soon.")
                            sleep(4)
                            exit()
                        elif exit_game == "n":
                            type_text("Awesome, continue where you left off")
                            break
                        else:
                            type_text("Please enter Y for yes or N for no")
                        continue

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
                print(f"{player_name}'s hand total: {player_hand_amount}")
                print("House hand total:", house_hand_amount)
                print()
                sleep(1)
                input("Press Enter to continue...")
                return True
            elif house_hand.total() > 21:
                type_text("The House has gone bust! You win this round.")
                print(f"{player_name}'s hand total: {player_hand_amount}")
                print("House hand total:", house_hand_amount)
                print()
                sleep(1)
                input("Press Enter to continue...")
                return True
            elif house_hand.equals_blackjack():
                type_text(
                    "The House has Blackjack, They win, better luck next time")
                print(f"{player_name}'s hand total: {player_hand_amount}")
                print("House hand total:", house_hand_amount)
                print()
                sleep(1)
                input("Press Enter to continue...")
                return True
            elif player_hand.equals_blackjack():
                type_text("WOW, you've got Blackjack, you win")
                print(f"{player_name}'s hand total: {player_hand_amount}")
                print("House hand total:", house_hand_amount)
                print()
                sleep(1)
                input("Press Enter to continue...")
                return True
            elif player_hand.equals_blackjack() and \
                    house_hand.equals_blackjack():
                type_text(
                    "Shame, that was close but as mentioned before the House "
                    "always wins if both hands are Blackjack")
                print()
                sleep(1)
                input("Press Enter to continue...")
                return True
        else:
            if house_hand.total() > player_hand.total():
                type_text("The House wins this round!")
                print(f"{player_name}'s hand total: {player_hand_amount}")
                print("House hand total:", house_hand_amount)
                print()
                sleep(1)
                input("Press Enter to continue...")
            elif house_hand.total() == player_hand.total():
                type_text("It's a draw")
                print(f"{player_name}'s hand total: {player_hand_amount}")
                print("House hand total:", house_hand_amount)
                print()
                sleep(1)
                input("Press Enter to continue...")
            else:
                type_text("Great job, you win!")
                print(f"{player_name}'s hand total: {player_hand_amount}")
                print("House hand total:", house_hand_amount)
                print()
                sleep(1)
                input("Press Enter to continue...")
            return True
        return False


def welcome():
    """
    A few typed out lines to welcome the user
    and retrieve their name.
    """
    global player_name

    type_text("Welcome to Blackjack")
    print()
    type_text("Lets take some time to get to know each other \U0001F60A")
    while True:
        player_name = input("What's your name?\n").capitalize()
        if player_name == " ":
            type_text("Come on, that's not a proper name.")
            continue
        elif player_name == "Jack":
            type_text("I Love That Name!!")
        sleep(1)
        type_text(f"Hi {player_name} my name is Jack, nice to meet you!!")
        print()
        input("Press enter to continue...")
        clear()
        type_text(
            'Now we have that out the way, I just wanted to go over a \n'
            'couple of things about the game before we continue'
            '\n'
            '\n'
            'Firstly, Thank you for being here, '
            'I really hope you enjoy the game!'
            '\n'
            '\n'
            'Throughout the process of the game you can use '
            'upper case or lower case, the\n'
            'system will know exactly what you are trying to say.\n'
            'When you see a (Y/N), this means, '
            'please answer with y for yes or n for no'
            '\n'
            '\n'
            'After any input you make, hitting the enter key will take \n'
            'you to the next step if you have entered a valid input. \n'
            'Any invalid input will give you prompt to enter a valid input.'
            '\n'
            '\n'
            'So, grab your snacks, grab your drinks and let\'s play '
            'some Blackjack'
            '\n'
            )
        sleep(1)
        break


def game_rules():
    """
    To give the user the chance to read the rules
    or just go straight into the game.
    """
    while True:
        type_text(f"So {player_name}, would you like to read the rules?")
        read_rules = str(input("Y for yes or N for no?\n")).lower()
        if read_rules == "y":
            clear()
            type_text(
                "The rules are simple, hit 21 and you win....\n"
                "Well, unless the house has 21, then they win!\n"
                "Sorry, some rules suck and thats one of them.\n"
                "That's it really..."
                )
            sleep(2)
            print()
            # Joker emoji
            type_text("Just Joking \U0001F0CF")
            sleep(1)
            # Silly face emoji
            type_text("\U0001F92A \U0001F92A \U0001F92A \U0001F92A")
            print()
            type_text("Enough messing around....")
            print()
            type_text(
                "When prompted, let me know how many games "
                "you'd like to play\n"
                "You will then be dealt a hand containing 2 cards\n"
                "It's the total value we are interested in\n"
                "Don't worry, I'll do the maths for you"
                '\n'
                '\n'
                "Once you have your value of both your cards added together\n"
                "It will be your decision to use Hit or Stand when prompted\n"
                "Hit will deal you another card\n"
                "Stand will submit your hand\n"
                "As mentioned before, the aim is to get 21 or as close to "
                "without going over\n"
                "So, be careful, if you get 22, you bust."
                '\n'
                '\n'
                )
            input("Press Enter to continue...")
            type_text(
                '\n'
                '\n'
                "Rules regarding the house hand\n"
                "If you bust by going over 21, "
                "the house hand automatically wins\n"
                "If the house hand has 17 or above they have to Stand\n"
                "And if they have below 17 they have to Hit"
                '\n'
                '\n'
                "Card values\n"
                "Number cards have the value of the number on the card\n"
                '\n'
                "Example:\n3 of hearts \U00002665 = 3\n"
                "9 of clubs \U00002663 = 9\n"
                '\n'
                "Face cards (J,Q,K) all = 10 individually\n"
                "Example:\nJ of hearts \U00002665 + "
                "3 of clubs \U00002663 = a value of 13\n"
                '\n'
                "Ace (A) is the wild card, "
                "Ace can = 1 or 11\n"
                "The value of Ace is dependant on if you have gone over 21\n"
                '\n'
                "Example:\nAce + 5 of hearts \U00002665 = 16\n"
                '\n'
                "However, if you add another card with the value of 8\n"
                "The value would be 24 but the Ace would then be a 1\n"
                "giving you a total value of 14 (Ace (1) + 5 + 8 = 14)"
                '\n'
                '\n'
                "Got all that?\n"
                "Just keep playing... you'll get it eventually"
                '\n'
                '\n'
                )

            while True:
                """
                To run at the end of the rules if statement
                """
                time_to_play = str(
                    input("So... Shall we get going? (Y/N)\n")).lower()
                if time_to_play == "y":
                    clear()
                    return PlayGame()
                elif time_to_play == "n":
                    type_text(
                        "Ok cool, come back when you are ready to "
                        "BlackJack \U0001F601")
                    exit()
                else:
                    type_text("Please enter Y or N")
                continue
        elif read_rules == "n":
            clear()
            type_text("Ok, let's get straight to it!")
            break
        else:
            type_text("Please enter Y or N ")
        continue


def play_again():
    """
    To give the user a chance to play agian.
    """
    re_run = True
    while re_run:
        type_text("Would you like to play again? (Y/N)")
        go_again = str(input("\n")).lower()

        if go_again == "y":
            clear()
            type_text("Awesome, new game loading....")
            sleep(2)
            game_rules()
            run.games()
        elif go_again == "n":
            clear()
            type_text(
                f"Well it was nice to meet you {player_name}, thanks for "
                "playing.")
            exit()
        else:
            type_text("Please enter Y for yes or N for n")
        continue


def clear():
    """
    To clear the terminal for a more focused approach.
    Used https://www.geeksforgeeks.org/clear-screen-python/ 
    to help write this function.
    """ 
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


welcome()
game_rules()
run = PlayGame()
run.games()
play_again()
