import random
import meanings_dictionary

suits = ('Wands', 'Pentacles', 'Swords', 'Cups')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Page', 'Queen', 'King',
         'Knight')

major_arcanas = (
    'Fool', 'Magician', 'High Priestess', 'Empress', 'Emperor', 'Hierophant', 'Lovers', 'Chariot', 'Strength',
    'Hermit', 'Wheel of Fortune', 'Justice', 'Hanged Man', 'Death', 'Temperance', 'Devil', 'Tower', 'Star',
    'Moon', 'Sun', 'Judgement', 'World')

keywords_major = meanings_dictionary.major_key_dict
keywords_minor = meanings_dictionary.minor_key_dict


class MinorCard():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.keyword = keywords_minor[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

    def arcana(self):
        arcana = 'minor'
        return arcana

    def general_meaning(self):
        return self.keyword



class MajorCard():

    def __init__(self, major_arcana):
        self.major_arcana = major_arcana
        self.keyword = keywords_major[major_arcana]

    def __str__(self):
        return self.major_arcana

    def arcana(self):
        arcana = 'major'
        return arcana

    def general_meaning(self):
        return self.keyowrds_major[self.major_arcana]


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

# class CardMeaning():

#     def __init__(self):


# test_deck = Deck()
# test_deck.shuffle()
# # print(test_deck)

# card1 = test_deck.deal()
# print(card1)
# card2 = test_deck.deal()
# print(card2)
