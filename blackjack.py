import os
from deck import Deck
from hand import Hand
from bankroll import Bankroll

MAX_VALUE = 21

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_game_state(player_hand, dealer_hand, player_bet):
    clear_console()
    print("BLACK JACK TABLE\n")
    print("Dealer:")
    print(dealer_hand)
    print("\n")
    print(f"You - bet {player_bet}:")
    print(player_hand)
    print()

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
            print(f"\n{bankroll}")
            amount = int(input("How much would you like to bet? "))
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
        action = input("\nYour turn. Do you want to hit (h) or stay (s)? ")[0].lower()
        if action == "h":
            return True
        elif action == "s":
            return False
        else:
            print("Invalid choice.")

def wait_for_input():
    input("\nDealer's turn. Press any key to continue..")

def play_topup_or_quit(bankroll):
    while True:
        print(f"\nYour bankroll balance is {bankroll.balance}.")
        options_str = ("What do you want to do:\n" +
                       " - Play (p) another round\n" +
                       " - Add (a) value to bankroll\n" +
                       " - Quit (q) the table\n")
        action = input(options_str)[0].lower()
        if action == "p":
            return True
        elif action == "a":
            bankroll.deposit(get_deposit_amount())
            return play_topup_or_quit(bankroll)
        elif action == "q":
            return False
        else:
            print("Invalid choice.")

def topup_or_quit(bankroll):
    while True:
        print("\nYour bankroll is empty.")
        options_str = ("What do you want to do:\n" +
                       " - Add (a) value to bankroll\n" +
                       " - Quit (q) the table\n")
        action = input(options_str)[0].lower()
        if action == "a":
            bankroll.deposit(get_deposit_amount())
            return play_topup_or_quit(bankroll)
        elif action == "q":
            return False
        else:
            print("Invalid choice.")

def play_another_round(bankroll):
    if bankroll.has_balance():
        return play_topup_or_quit(bankroll)
    else:
        return topup_or_quit(bankroll)

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

def play_round(deck, player_bet):
    player_hand = Hand()
    dealer_hand = Hand(last_card_face_down=True)

    player_hand.take(deck.draw_card())
    dealer_hand.take(deck.draw_card())
    player_hand.take(deck.draw_card())
    dealer_hand.take(deck.draw_card())

    player_turn = True
    while player_turn:
        print_game_state(player_hand, dealer_hand, player_bet)
        
        if take_more():    
            player_hand.take(deck.draw_card())
        else:
            player_turn = False

        if player_hand.hand_sum() > MAX_VALUE:
            player_turn = False

    dealer_turn = True
    while dealer_turn:
        print_game_state(player_hand, dealer_hand, player_bet)

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
        bet = get_bet(player_bankroll)
        player_wins = play_round(deck, bet)

        if player_wins:
            player_bankroll.deposit(2*bet)

        if not play_another_round(player_bankroll):
            break

    print(f"You decided to leave the table with a bankroll of {player_bankroll.balance}.")
    print("Thank you for playing!")

if __name__ == "__main__":
    start_game()
