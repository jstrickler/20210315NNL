import random

class CardDeck:
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer_name):
        # self.variable_name = some_value
        self.dealer = dealer_name  # store dealer_name in ._dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    @property
    def dealer(self):  # public getter property
        # return self._get_name_from_db(self._dealer)
        return self._dealer  # return private data

    @dealer.setter  # public setter property
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer   # update private data
        else:
            raise TypeError("Dealer must be a string")

    def get_dealer(self):
        return self._dealer

    def shuffle(self):
        random.shuffle(self._cards)