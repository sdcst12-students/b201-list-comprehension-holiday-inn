#!python3
import random


ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
suits = ['H','C','S','D']

deck = [f"{j}{i}" for i in suits for j in ranks]
z = round((len(deck)/2))
fdeck = deck[0:z]
sdeck = deck[z:]
sdeck.reverse()

print(fdeck +sdeck)





def shuf(deck):
    random.shuffle(deck)
    return deck
def draws():
    shuf()
    many = int(input("how many cards would you like to draw?: "))
    draw = []
    for i in range(many):
        draw.append(deck[i])
        deck.pop(i)
    return draw
# a-k h, c, k-a d ,s



