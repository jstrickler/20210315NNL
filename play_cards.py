from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Leonard")
print(d1)
print(type(d1))
d2 = CardDeck("Wanda")
print(d2)

print(d1.dealer)
print(d1.get_dealer())

d1.dealer = "Monty"
print(d1.dealer)

try:
    d1.dealer = 123.456
except TypeError as err:
    print(err)
else:
    print(d1.dealer.upper())

d1.shuffle()
print(d1.cards, '\n')

j1 = JokerDeck("Albert")
j1.shuffle()
print(j1.cards, '\n')
