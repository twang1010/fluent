from collections import MutableSequence
from collections import namedtuple

Card = namedtuple('Card',['rank','suit'])


class FrenchDeck2(MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ('spades', 'diamonds', 'clubs', 'hearts')

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                                       for suit in self.suits]

    def __getitem__(self, position):
        return self._cards[position]

    def __len__(self):
        return len(self._cards)

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __delitem__(self, position):
        del self._cards[position]

    def insert(self, index, value):
        self._cards.insert(index, value)

# Test French Deck #

deck = FrenchDeck2()
for card in deck:
    print(card)
