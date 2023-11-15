import random
import create_deck

deck = create_deck.Deck()
deck.shuffle()


class QuickFocus():

    def __init__(self):
        self.current_you_card = deck.deal()
        self.obstacle_card = deck.deal()
        self.focus_on_card = deck.deal()
        self.let_go_card = deck.deal()

    def __str__(self):
        return 'Where you are currently = {}, Your obstacle = {}, Focus on = {}, Let go of = {}'.format(
            self.current(), self.obstacle(), self.focus(), self.let_go())

    def current(self):
        return self.current_you_card

    def obstacle(self):
        return self.obstacle_card

    def focus(self):
        return self.focus_on_card

    def let_go(self):
        return self.let_go_card

    @property
    def card_amount(self):
        return 4

