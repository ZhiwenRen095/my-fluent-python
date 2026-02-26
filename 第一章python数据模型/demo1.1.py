"""实现 __getitem__ 和 __len__ 魔术方法"""
import collections
from random import choice

Card = collections.namedtuple('Card', ['rand', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __contains__(self, card):
        return card in self._cards


def spades_high(card: Card):
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    rank_value = FrenchDeck.ranks.index(card.rand)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    deck = FrenchDeck()

    # 测试in   __contains__
    my_card = Card('2', 'spades')
    print(my_card in deck)

    # 测试切片  __getitem__
    print(deck[:3])
    print(deck[12::13])

    # 测试循环  __contains__
    for card in reversed(deck):
        print(card)

    # 随机摸一张牌
    print("随机摸一张牌")
    print(choice(deck))
    print("=" * 88)

    # 排序
    for card in sorted(deck, key=spades_high):
        print(card)
