import random
import create_deck
import create_spreads
import meanings_dictionary

keywords_major = meanings_dictionary.major_key_dict

keywords_minor = meanings_dictionary.minor_key_dict

deck = create_deck.Deck()
card1 = deck.shuffle()

print(card1)


deck.deal()

# print(deck)
# print(str(deck))
# print()





