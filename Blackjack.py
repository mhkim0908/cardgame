#written with python 3.10.2 64-bit 
import random

class Card:
    def __init__ (self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()  # if use ACE as 11 points = soft, elif use ACE  as 1 point = hard
    
class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)

class AceCard(Card):
    def _points(self):
        return 1, 11
    
class FaceCard(Card):
    def _points(self):
        return 10, 10

def cards(rank,suit):
    if rank == 1:
        return AceCard('A',suit)
    elif 2<= rank < 11 :
        return NumberCard(str(rank),suit)
    elif rank == 11:
        return FaceCard('J',suit)
    elif rank == 12:
        return FaceCard('Q',suit)
    elif rank == 13:
        return FaceCard('K',suit)
    else:
        raise Exception("Rank out of range")

#deck = [cards(rank,suit)                    # Make 52 cards 
#        for rank in range(1,14) 
#            for suit in ('♣', '◆', '♥', '♠')]

class Deck:
    def __init__(self):                     
        self._cards = [cards(rank,suit) for rank in range(1,14) for suit in ('♣', '◆', '♥', '♠')]
        random.shuffle(self._cards)
    
    def pop(self):
        return self._cards.pop()

#d = Deck()
#hand = [d.pop(), d.pop()]

#print(hand[0].rank,hand[0].suit,hand[1].rank,hand[1].rank)


class Deck2(list):
    def __init__(self, decks=6):             #Empty collection
        super().__init__                   #get parent's(in here, 'list') class' __init__
        for i in range(decks): 
            self.extend(cards(rank,suit) for rank in range(1,14) for suit in ('♣', '◆', '♥', '♠'))       #extend shoe(6 deck)
        random.shuffle(self)
        burn=random.randint(1,52)             # It means discarding the few first cards without playing it before the start of the game.
        for i in range(burn): 
            self.pop()  
        

class Hand:
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self.cards = list(cards)

    def hand_total(self):
        return sum(c.hand for c in self.cards)
    
    def soft_total(self):
        return sum(c.hand for c in self.cards)

#d2 = Deck2()
#h = Hand(d.pop(),d.pop(),d.pop())

#print(h.cards[0].rank)

class Hand5:
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self.cards = list(cards)
    @staticmethod
    def freeze(other):
        hand = Hand5(other.dealer_card, *other.cards)
        return hand
    @staticmethod
    def split(other, card0, card1):
        hand0 = Hand5(other.dealer_card, other.cards[0], card0)
        hand1 = Hand5(other.dealer_card, other.cards[1], card1)
        return hand0, hand1
    def __str__(self):
        return ",".join(map(str, self.cards))

d = Deck()
h = Hand5(d.pop(),d.pop(),d.pop())
s1, s2 = Hand5.split(h,d.pop(),d.pop())

#print(s1.cards[0].rank,s1.cards[0].suit, s2.cards[0].rank)