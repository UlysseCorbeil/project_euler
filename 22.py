import os

local_file = os.path.join(os.path.dirname(__file__), '22.txt')

file = open(local_file,  "r")

data = file.read().replace('"', "").replace("\n", "").split(",")

_alph = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}

def g_score(names):

    l_names = []

    for ind, name in enumerate(names):
        l_names.append([str(k) for k in str(name)])

    s_l_names = sorted(l_names)
    score = 0
    index = 0
    for splitted_name in s_l_names:
        index += 1
        for letter in splitted_name:
            score += _alph[letter] * index
    return score

print(g_score(data))
