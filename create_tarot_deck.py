import random
import meanings_dictionary

import cards

full_deck_dict = meanings_dictionary.all_full_dict
card_list = cards.cards_full_list


class TarotCards():

    def __init__(self, card):
        self.card = card
        self.arcana_type = ''
        self.meaning = full_deck_dict[self.card]

    def __str__(self):
        return self.card

    def arcana(self):
        if self.card in card_list[:22]:
            self.arcana_type = 'major'
        if self.card not in card_list[:22]:
            self.arcana_type = 'minor'
        return self.arcana_type

    def main_meaning(self):
        return self.meaning


class TarotDeck():

    def __init__(self):
        # self.cards = card_list
        self.deck = card_list


    def __str__(self):
        deck_compile = ''
        # for card in self.deck:
        for card in self.deck:
            deck_compile += '\n' + card.__str__()
        return 'This deck has:' + deck_compile


    def shuffle(self):
        random.shuffle(card_list)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

    def list_cards(self):
        deck_compile_list = ''
        for card in card_list:
            deck_compile_list += card.__str__() + ','
            final_card_list = deck_compile_list[: len(deck_compile_list) - 2]
        return final_card_list.split(',')





