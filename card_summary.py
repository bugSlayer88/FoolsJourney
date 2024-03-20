import csv

with open('sql/exports/card_meaning.csv', mode='r') as file:
    card_meanings = csv.reader(file)
    card_mean_lines = []
    for lines in card_meanings:
        card_mean_lines.append(lines)


# what well need to know
# each card
# total cards pulled

# create a list of strings based on sql csv of cards pulled
def build_card_list(cards_pulled):
    build_list = []
    for i in range(len(card_mean_lines)):
        for card in cards_pulled:
            if card_mean_lines[i][1] == card:
                build_list.append(card_mean_lines[i])

    return build_list


# assess special built list of cards to get majors

def get_majors(cards_pulled_list):
    majors_pulled = []
    for i in range(len(cards_pulled_list)):
        if cards_pulled_list[i][4] == 't':
            majors_pulled.append(cards_pulled_list[i][1])

    return majors_pulled


# assess special built list of cards to get minors

def get_minors(cards_pulled_list):
    minors_pulled = []
    for i in range(len(cards_pulled_list)):
        if cards_pulled_list[i][4] == 'f':
            minors_pulled.append(cards_pulled_list[i][1])

    return minors_pulled


def get_aces(cards_pulled_list):
    aces_pulled = []
    for i in range(len(cards_pulled_list)):
        if 'Ace' in cards_pulled_list[i][1]:
            aces_pulled.append(cards_pulled_list[i][1])

    return aces_pulled

def get_kings(cards_pulled_list):
    kings_pulled = []
    for i in range(len(cards_pulled_list)):
        if 'King' in cards_pulled_list[i][1]:
            kings_pulled.append(cards_pulled_list[i][1])

    return kings_pulled

def get_queens(cards_pulled_list):
    queens_pulled = []
    for i in range(len(cards_pulled_list)):
        if 'Queen' in cards_pulled_list[i][1]:
            queens_pulled.append(cards_pulled_list[i][1])

    return queens_pulled


# cards_pulled_test = ['King of Coins', 'Queen of Swords', 'Empress', 'Magician', 'Three of Wands', 'Ten of Coins', 'World', 'Ace of Wands']
#
# build_list = build_card_list(cards_pulled_test)
#
# majors_test = get_majors(build_list)
# minors_test = get_minors(build_list)
# aces_test = get_aces(build_list)
# kings_test = get_kings(build_list)
#
# print(majors_test)
# print(minors_test)
# print(aces_test)
# print(kings_test)