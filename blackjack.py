from deck import Deck
from hand import Hand
from bankroll import Bankroll
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

def get_deposit_amount():
    while True:
        try:
            amount = int(input("\nHow much would you like to add to your bankroll? "))
            if amount > 0:
                return amount
            else:
                print("The amount needs to be greater than 0.")    
        except:
            print("Invalid amount. Please enter an integer greater than 0.")

def get_bet(bankroll):
    while True:
        try:
            amount = int(input("\nHow much would you like to bet? "))
            if amount > 0:
                try:
                    bankroll.withdraw(amount)
                    return amount
                except ValueError:
                    print(f"Insufficient balance. {bankroll}.")
            else:
                print("The amount needs to be greater than 0.")    
        except:
            print("Invalid amount. Please enter an integer greater than 0.")


def take_more():
    while True:
        action = input("\nYour turn. Do you want to hit (h) or stay (s)? ")
        if action == "h":
            return True
        elif action == "s":
            return False
        else:
            print("Invalid choice.")

def wait_for_input():
    input("\nDealer's turn. Press any key to continue..")

def does_player_win(player_sum, dealer_sum):
    if player_sum > MAX_VALUE:
        print("You BUST, you lose!")
        return False
    elif dealer_sum > MAX_VALUE:
        print(f"You have {player_sum}, dealer BUST. You win!")
        return True
    elif dealer_sum > player_sum:
        print(f"You have {player_sum}, dealer has {dealer_sum}. You lose!")
        return False
    else:
        print(f"You have {player_sum}, dealer has {dealer_sum}. You win!")
        return True

def play_round(deck):
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
    
    return does_player_win(player_hand.hand_sum(), dealer_hand.hand_sum())

def start_game():
    clear_console()
    print("Welcome to the Black Jack table!")

    deck = Deck()
    deck.shuffle()

    player_bankroll = Bankroll()
    player_bankroll.deposit(get_deposit_amount())
    
    while True:
        if not player_bankroll.has_balance():
            print("Your bankroll is empty. Game over!")
            break

        print(f"\n{player_bankroll}")
        bet = get_bet(player_bankroll)
        player_wins = play_round(deck)

        if player_wins:
            player_bankroll.deposit(2*bet)

if __name__ == "__main__":
    start_game()
