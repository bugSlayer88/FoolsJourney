import random
import create_deck

deck = create_deck.Deck()
deck.shuffle()

class SimpleThreeCardSpread():

    def __init__(self):
        pass

    def __str__(self):
        return 'Past = {}, Present = {}, Future = {}'.format(self.past_card(),self.present_card(),
                                                             self.future_card())

    def past_card(self):
        past = deck.deal()
        return past

    def present_card(self):
        present = deck.deal()
        return present

    def future_card(self):
        future = deck.deal()
        return future
    
    
current_you = deck.deal()
obstacle = deck.deal()
focus_on = deck.deal()
let_go = deck.deal()

class QuickFocusSpread():

    def __init__(self, current_you, obstacle, focus_on, let_go):
        self.current_you = current_you
        self.obstacle = obstacle
        self.focus_on = focus_on
        self.let_go = let_go
    
    def __str__(self):
         return 'Where you are currently = {}, Your obstacle = {}, Focus on = {}, Let go of = {}'.format(
             self.current_you,self.obstacle,self.focus_on,self.let_go)