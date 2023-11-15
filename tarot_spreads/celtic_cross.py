import random
import create_deck

deck = create_deck.Deck()
deck.shuffle()


class CelticCross():

    def __init__(self):
        self.your_influence_card = deck.deal()
        self.obstacle_card = deck.deal()
        self.best_outcome_card = deck.deal()
        self.foundation_card = deck.deal()
        self.past_card = deck.deal()
        self.future_card = deck.deal()
        self.pres_card = deck.deal()
        self.home_card = deck.deal()
        self.hope_fear_card = deck.deal()
        self.answer_card = deck.deal()

    def __str__(self):
        return ('{}'.format(self.your_influence_card()))

    def influence_now(self):
        return self.your_influence_card

    def obstacle(self):
        return self.obstacle_card

    def outcome(self):
        return self.best_outcome_card

    def foundation(self):
        return self.foundation_card
