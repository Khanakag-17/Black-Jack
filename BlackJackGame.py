import random

# Check if player & dealer are still in the game
player_in = True
dealer_in = True

# Deck of cards and player & dealer's hand
deck_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
dealer_hand = []
player_hand = []

# Deal the cards
def deal_card(turn):
    cards = random.choice(deck_cards)
    turn.append(cards)
    deck_cards.remove(cards)

# Calculate the total of hand
def calc_total(turn):
    sum = 0
    face_cards = ['J', 'K', 'Q']

    for card in turn:
        if(card in face_cards):
            sum += 10
        elif card in range(2, 11):
            sum += card
        else:
            if sum > 11:
                sum += 1
            else:
                sum += 11

    return sum

# Check for winner
def dealer_hand_check():
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    elif len(dealer_hand) > 2:
        return dealer_hand[0], dealer_hand[1]

# Main game
for _ in range(2):
    deal_card(dealer_hand)
    deal_card(player_hand)

while player_in or dealer_in:
    print(f"Dealer had {dealer_hand_check()}.")
    print(f"You have {player_hand} for a total of {calc_total(player_hand)}.")

    if player_in:
        stay_hit = int(input("1: Stay \n2: Hit \n"))

    if calc_total(dealer_hand) > 21:
        dealer_in = False
    else: 
        deal_card(dealer_hand)

    if stay_hit == 2:
        player_in = False
    else:
        deal_card(player_hand)


    if calc_total(player_hand) >= 21:
        break
    elif calc_total(dealer_hand) >= 21:
        break

if calc_total(player_hand) == 21:
    print(f"\nYou had {player_hand} with a total of {calc_total(player_hand)}. 
          \nDealer had {dealer_hand} with a total of {calc_total(dealer_hand)}.")
    print("BlackJack! You win.")

elif calc_total(dealer_hand) == 21:
    print(f"\nYou had {player_hand} with a total of {calc_total(player_hand)}. 
          \nDealer had {dealer_hand} with a total of {calc_total(dealer_hand)}.")
    print("BlackJack! Dealer wins.")

elif calc_total(player_hand) > 21:
    print(f"\nYou had {player_hand} with a total of {calc_total(player_hand)}. 
          \nDealer had {dealer_hand} with a total of {calc_total(dealer_hand)}.")
    print("You bust. Dealer wins!")

elif calc_total(dealer_hand) > 21:
    print(f"\nYou had {player_hand} with a total of {calc_total(player_hand)}. 
          \nDealer had {dealer_hand} with a total of {calc_total(dealer_hand)}.")
    print("Dealer busts. You win!")

elif 21 - calc_total(player_hand) > 21 - calc_total(dealer_hand):
    print(f"\nYou had {player_hand} with a total of {calc_total(player_hand)}. 
          \nDealer had {dealer_hand} with a total of {calc_total(dealer_hand)}.")
    print("Dealer wins!")

else:
    print(f"\nYou had {player_hand} with a total of {calc_total(player_hand)}. 
          \nDealer had {dealer_hand} with a total of {calc_total(dealer_hand)}.")
    print("You win!")