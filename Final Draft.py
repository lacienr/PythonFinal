# Blackjack I hope


#Opening Prompts
print("Welcome to the Blackjack Table!")
print("Good Luck! You'll need it!stand")
print("Lets Gamble!")
#import random for dealing and shuffle
import random

# Create deck shuffle
def create_deck():
    deck = []
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}')
    random.shuffle(deck)
    return deck

# Get values of the cards
def get_value(card):
    if card.startswith(('2', '3', '4', '5', '6', '7', '8', '9', '10')):
        return int(card.split()[0])
    elif card.startswith(('Jack', 'Queen', 'King')):
        return 10
    else:
        return 11

# Get values of hands total and figure out the Ace 
def get_hand_value(hand):
    value = 0
    for card in hand:
        value += get_value(card)
    for card in hand:
        if card.startswith('Ace') and value > 21:
            value -= 10
    return value

# Deal
def deal_card(deck):
    return deck.pop()

# Lets gamble!
def play_game():
    deck = create_deck()
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    print(f"Dealer's upcard: {dealer_hand[0]}")
    while True:
        print(f"Your hand: {player_hand} ({get_hand_value(player_hand)})")
        action = input("Do you want to hit or stand? ")
        if action.lower() == 'hit':
            player_hand.append(deal_card(deck))
            if get_hand_value(player_hand) > 21:
                print(f"Your hand: {player_hand} ({get_hand_value(player_hand)})")
                print("BUSTTTTTT! Dealer wins!")
                return
        elif action.lower() == 'stand':
            print(f"Dealer's hand: {dealer_hand} ({get_hand_value(dealer_hand)})")
            while get_hand_value(dealer_hand) < 17:
                dealer_hand.append(deal_card(deck))
            print(f"Dealer's final hand: {dealer_hand} ({get_hand_value(dealer_hand)})")
            if get_hand_value(dealer_hand) > 21:
                print("Dealer busted! WINNER!")
                return
            elif get_hand_value(dealer_hand) > get_hand_value(player_hand):
                print("Dealer wins!")
                return
            elif get_hand_value(dealer_hand) == get_hand_value(player_hand):
                print("Push! Try again!")
                return
            else:
                print("WINNER!")
                return

# play again
while True:
    play_game()
    answer = input("Do you want to play again? ")
    if answer.lower() != 'yes':
        break
print("Thanks for playing!")

