import random

def should_hit(dealer_total, player_total):
    return True if (player_total < 17 and dealer_total > 6) or player_total < 12 else False

def deal(cards):
    return random.choice(cards)

def integer(x):
    if x == "J" or x == "Q" or x == "K":
        return 10
    elif x == "A":
        return 11
    else: return int(x)

def dealer_min(dealer_total):
    while dealer_total < 17:
        new_card = integer(deal(cards))
        dealer_total += new_card
    return dealer_total

cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

#PLAYERS
first_card = deal(cards)
player_first = integer(first_card)

second_card = deal(cards)
if second_card == "A" and first_card == "A":
    player_second = 1
else: player_second = integer(second_card)

print("Players:")
print("First card is : %s" %first_card)
print("Second card is : %s" %second_card)

player_total = player_first + player_second
print("Player total card is : %d" %player_total)

#DEALERS
first_card = deal(cards)
dealer_first = integer(first_card)

print("")
print("Dealers:")
print("First card is : %s" %first_card)
print("")

while should_hit(dealer_first, player_total) == True:
    new_card = integer(deal(cards))
    print("Next dealt card is : %d" %new_card)
    player_total += new_card

print("Player total card is : %d" %player_total)

if player_total > 21:
    exit("Player busted!")

second_card = deal(cards)
dealer_second = integer(second_card)

print("")
print("Dealers")
print("First card is : %s" %first_card)
print("Second card is : %s" %second_card)
dealer_total = dealer_first + dealer_second
print("Dealer total card is : %d" %dealer_total)

dealer_total = dealer_min(dealer_total)
print("Dealer total card is : %d" %dealer_total)
