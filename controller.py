from PyQt6 import QtCore, QtGui, QtWidgets
import create_deck
import create_spreads
import meanings_dictionary

deck = create_deck.Deck()
deck.shuffle()
simple_spread = create_spreads.SimpleThreeCard()
keywords_major = meanings_dictionary.major_key_dict
keywords_minor = meanings_dictionary.minor_key_dict

# creating these now so that the card is drawn only once
# should I get this from the ui or should i figure out how to only run the function once?
past_card = simple_spread.past_card()
present_card = simple_spread.present_card()
future_card = simple_spread.future_card()


