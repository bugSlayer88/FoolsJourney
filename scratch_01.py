import random
import create_deck
import create_spreads
import meanings_dictionary

keywords_major = meanings_dictionary.major_key_dict

keywords_minor = meanings_dictionary.minor_key_dict

deck = create_deck.Deck()
deck.shuffle()

# print(deck)

# card1 = deck.deal()
# print(card1)
# print(card1.keyword)
#
# card2 = deck.deal()
# print(card2)
# print(card2.keyword)
#
card3 = deck.deal()
# print(card3)
# print(card3.keyword)


simple = create_spreads.SimpleThreeCardSpread()
past_card = simple.past_card()
print(past_card)
print(past_card.keyword)


# print(simple.past_card())
# print(simple.present_card())
# print(simple.future_card())

# print(simple)