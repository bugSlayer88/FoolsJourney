import csv

with open('sql/exports/card_meaning.csv', mode='r') as file:
    card_meanings = csv.reader(file)
    card_mean_lines = []
    for lines in card_meanings:
        card_mean_lines.append(lines)


def get_general_meaning(card):
    basic_meaning = []
    for i in range(len(card_mean_lines)):
        if card_mean_lines[i][1] == card:
            basic_meaning.append(card_mean_lines[i][2])

    return basic_meaning[0]


def get_negative_meaning(card):
    negative_meaning = []
    for i in range(len(card_mean_lines)):
        if card_mean_lines[i][1] == card:
            negative_meaning.append(card_mean_lines[i][3])

    return negative_meaning[0]
