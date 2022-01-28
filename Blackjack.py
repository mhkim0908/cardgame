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



cards = [AceCard('A', 'spade'),NumberCard('2','spade'),NumberCard('3','spade')]

print(cards[0]._points())