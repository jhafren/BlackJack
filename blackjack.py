from deck import Deck
from hand import Hand
import os

MAX_VALUE = 21

def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')

def print_game_state(player_hand, dealer_hand):
    clear_console()
    print("BLACK JACK TABLE\n")
    print("Dealer:")
    print(dealer_hand)
    print("\n")
    print("You:")
    print(player_hand)
    print("\n")

def take_more():
    while True:
        action = input("\nYour turn. Do you want to take (t) or stay (s)? ")
        if action == "t":
            return True
        elif action == "s":
            return False
        else:
            print("Invalid choice.")

def wait_for_input():
    input("\nDealer's turn. Press any key to continue..")

def determine_winner(player_sum, dealer_sum):
    if player_sum > MAX_VALUE:
        print("You BUST, you lose!")
    elif dealer_sum > MAX_VALUE:
        print(f"You have {player_sum}, dealer BUST. You win!")
    elif dealer_sum > player_sum:
        print(f"You have {player_sum}, dealer has {dealer_sum}. You lose!")
    else:
        print(f"You have {player_sum}, dealer has {dealer_sum}. You win!")

def start_game():
    print("Welcome to the Black Jack table!")
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    dealer_hand = Hand(last_card_face_down=True)

    player_hand.take(deck.draw_card())
    dealer_hand.take(deck.draw_card())
    player_hand.take(deck.draw_card())
    dealer_hand.take(deck.draw_card())

    player_turn = True
    while player_turn:
        print_game_state(player_hand, dealer_hand)
        
        if take_more():    
            player_hand.take(deck.draw_card())
        else:
            player_turn = False

        if player_hand.hand_sum() > MAX_VALUE:
            player_turn = False

    dealer_turn = True
    while dealer_turn:
        print_game_state(player_hand, dealer_hand)

        if (player_hand.hand_sum() <= MAX_VALUE and
                dealer_hand.hand_sum() < MAX_VALUE and
                dealer_hand.hand_sum() <= player_hand.hand_sum()):

            wait_for_input()
            if dealer_hand.last_card_face_down:
                dealer_hand.show_last_card()
            else:
                dealer_hand.take(deck.draw_card())
        else:
            dealer_turn = False
    
    determine_winner(player_hand.hand_sum(), dealer_hand.hand_sum())

if __name__ == "__main__":
    start_game()
