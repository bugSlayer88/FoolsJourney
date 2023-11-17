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

    def quick_summary(self):
        card_list = [self.past(), self.present(), self.future()]

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

        return '{} Majors\n{} Minors\n{} Receptive Cards\n{} Active Cards\n{} Neutral Cards'.format(major_count, minor_count, receptive_count, active_count, neutral_count)