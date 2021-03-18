from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()  # call method in parent
        for joker_num in '1', '2':
            card = joker_num, '*JOKER*'
            self._cards.append(card)
