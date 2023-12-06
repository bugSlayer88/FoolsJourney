import random
import meanings_dictionary

suits = ('Wands', 'Coins', 'Swords', 'Cups')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Page', 'Queen', 'King',
         'Knight')

major_arcanas = (
    'Fool', 'Magician', 'High Priestess', 'Empress', 'Emperor', 'Hierophant', 'Lovers', 'Chariot', 'Justice',
    'Hermit', 'Wheel of Fortune', 'Strength', 'Hanged Man', 'Death', 'Temperance', 'Devil', 'Tower', 'Star',
    'Moon', 'Sun', 'Judgement', 'World')

# keywords_major = meanings_dictionary.major_key_dict
# keywords_minor = meanings_dictionary.minor_key_dict
#
# main_meaning_minor = meanings_dictionary.minor_full_dict
# main_meaning_major = meanings_dictionary.major_full_dict

all_meanings = meanings_dictionary.all_full_dict

suits_major = meanings_dictionary.major_suit_dict
ranks_major = meanings_dictionary.major_rank_dict

modality_type = meanings_dictionary.modality_dict


class MinorCard():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.arcana_type = 'minor'
        # self.keyword = keywords_minor[rank]
        self.meaning = all_meanings[rank + ' of ' + suit]
        self.modality_type = modality_type[suit]

    def __str__(self):
        return self.rank + ' of ' + self.suit

    def arcana(self):
        return self.arcana_type

    # def general_meaning(self):
    #     return self.meaning

    def main_meaning(self):
        return self.meaning

    def modality(self):
        return self.modality_type


class MajorCard():

    def __init__(self, major_arcana):
        self.major_arcana = major_arcana
        # self.keyword = keywords_major[major_arcana]
        self.meaning = all_meanings[major_arcana]
        self.arcana_type = 'major'
        self.suit = suits_major[major_arcana]
        self.rank = ranks_major[major_arcana]
        self.modality_type = modality_type[major_arcana]

    def __str__(self):
        return self.major_arcana

    def arcana(self):
        return self.arcana_type

    # def general_meaning(self):
    #     return self.keyword

    def main_meaning(self):
        return self.meaning

    def modality(self):
        return self.modality_type


class Deck():

    def __init__(self):
        self.deck = []
        for major_arcana in major_arcanas:
            self.deck.append(MajorCard(major_arcana))
        for suit in suits:
            for rank in ranks:
                self.deck.append(MinorCard(suit, rank))

    def __str__(self):
        deck_compile = ''
        for card in self.deck:
            deck_compile += '\n ' + card.__str__()
        return 'The deck has:' + deck_compile

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

    def list_cards(self):
        # all_cards = []
        # for card in self.deck:
        #     all_cards = str(card)
        # return all_cards
        deck_compile_list = ''
        for card in self.deck:
            deck_compile_list += card.__str__() + ','
        return deck_compile_list.split(',')
