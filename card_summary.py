import csv

with open('sql/exports/card_meaning.csv', mode='r') as file:
    card_meanings = csv.reader(file)
    card_mean_lines = []
    for lines in card_meanings:
        card_mean_lines.append(lines)


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

def get_pages(cards_pulled_list):
    pages_pulled = []
    for i in range(len(cards_pulled_list)):
        if 'Page' in cards_pulled_list[i][1]:
            pages_pulled.append(cards_pulled_list[i][1])

    return pages_pulled

def get_knights(cards_pulled_list):
    knights_pulled = []
    for i in range(len(cards_pulled_list)):
        if 'Knight' in cards_pulled_list[i][1]:
            knights_pulled.append(cards_pulled_list[i][1])

    return knights_pulled

def get_courts(cards_pulled_list):
    courts_pulled= []
    for i in range(len(cards_pulled_list)):
        if cards_pulled_list[i][6] == 't':
            courts_pulled.append(cards_pulled_list[i][1])

    return courts_pulled

def get_card_numbers(cards_pulled_list):
    numbers_list = []
    for i in range(len(cards_pulled_list)):
        card_number = cards_pulled_list[i][7]
        numbers_list.append(card_number)

    ones = numbers_list.count('1')
    twos = numbers_list.count('2')
    threes = numbers_list.count('3')
    fours = numbers_list.count('4')
    fives = numbers_list.count('5')
    sixes = numbers_list.count('6')
    sevens = numbers_list.count('7')
    eights = numbers_list.count('8')
    nines = numbers_list.count('9')
    tens = numbers_list.count('10')

    card_num_tally = {
        "ones": ones,
        "twos": twos,
        "threes": threes,
        "fours": fours,
        "fives": fives,
        "sixes": sixes,
        "sevens": sevens,
        "eights": eights,
        "nines": nines,
        "tens": tens
    }

    del_keys = []
    for key, value in card_num_tally.items():
        if value == 0:
            del_keys.append(key)
    for key in del_keys:
        card_num_tally.pop(key)

    return card_num_tally


cards_pulled_test = ['King of Coins', 'Queen of Swords', 'Empress', 'Magician', 'Three of Wands', 'Ten of Coins', 'World', 'Ace of Wands', 'Hierophant', 'Seven of Coins', 'Knight of Wands', 'Page of Coins', 'Queen of Cups']
# #
build_list = build_card_list(cards_pulled_test)
print(build_list)
number_test = get_card_numbers(build_list)
print(number_test)
# #
# majors_test = get_majors(build_list)
# minors_test = get_minors(build_list)
# aces_test = get_aces(build_list)
# kings_test = get_kings(build_list)
# pages_test = get_pages(build_list)
# knights_test = get_knights(build_list)
# court_test = get_courts(build_list)
# #
# print(majors_test)
# print(minors_test)
# print(aces_test)
# print(kings_test)
# print(pages_test)
# print(knights_test)
# print(court_test)

# if 'King' in cards_pulled_test[0]:
#     print('yessir')