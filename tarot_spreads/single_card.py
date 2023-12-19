import create_deck
import create_tarot_deck

# deck = create_deck.Deck()

deck = deck_redo.TarotDeck()

deck.shuffle()


class SingleCard():

    def __init__(self):
        self.single_card = deck.deal()

    def __str__(self):
        return 'Card = {}'.format(self.single())

    def single(self):
        return self.single_card
