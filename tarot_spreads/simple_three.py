import random
import create_deck

deck = create_deck.Deck()
deck.shuffle()


class SimpleThreeCard():

    def __init__(self):
        self.past_card = deck.deal()
        self.present_card = deck.deal()
        self.future_card = deck.deal()

    def __str__(self):
        return 'Past = {}, Present = {}, Future = {}'.format(self.past(), self.present(), self.future())

    def past(self):
        return self.present_card

    def present(self):
        return self.present_card

    def future(self):
        return self.future_card

    @property
    def card_amount(self):
        return 3
