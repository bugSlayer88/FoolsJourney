import random
import create_deck
import deck_redo

# deck = create_deck.Deck()
deck = deck_redo.TarotDeck()
deck.shuffle()

class Momentum():

    def __init__(self):
        self.now_card = deck.deal()
        self.obstacle_card = deck.deal()
        self.past_card = deck.deal()
        self.present_card = deck.deal()
        self.future_card = deck.deal()
        self.let_go_card = deck.deal()
        self.focus_on_card = deck.deal()

    def __str__(self):
        return ('You now = {}\nYour obstacle = {}\nFocus on = {}\nLet go of = {}\nPast = {}\nPresent = {}\n'
                'Future = {}').format(self.person_now(), self.obstacle_now(), self.focus_on(), self.let_go_of(),
                                      self.past(), self.present(), self.future())

    def person_now(self):
        return self.now_card

    def obstacle_now(self):
        return self.obstacle_card

    def past(self):
        return self.past_card

    def present(self):
        return self.present_card

    def future(self):
        return self.future_card

    def focus_on(self):
        return self.focus_on_card

    def let_go_of(self):
        return self.let_go_card

    @property
    def card_amount(self):
        return 7

    def quick_summary(self):
        card_list = [self.person_now(), self.obstacle_now(), self.past(), self.present(),
                     self.future(), self.focus_on(), self.let_go_of()]

        arcana_here = []
        for i in range(len(card_list)):
            arcana_category = card_list[i].arcana()
            arcana_here.append(arcana_category)

        modes_here = []
        for i in range(len(card_list)):
            mode_category = card_list[i].modality()
            modes_here.append(mode_category)

        major_count = arcana_here.count('major')
        minor_count = arcana_here.count('minor')

        receptive_count = modes_here.count('Receptive')
        active_count = modes_here.count('Active')
        neutral_count = modes_here.count('Neutral')

        return '{} Majors\n{} Minors\n{} Receptive Cards\n{} Active Cards\n{} Neutral Cards'.format(major_count,
                                                                                                    minor_count,
                                                                                                    receptive_count,
                                                                                                    active_count,
                                                                                                    neutral_count)

