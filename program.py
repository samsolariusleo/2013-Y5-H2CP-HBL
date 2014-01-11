# Filename: program.py
# Author: Gan Jing Ying
# Created: 20131125
# Modified: 20131125

import random

# initiate variables
scores = []
alphas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# generates a list of usernames and scores
def genlist(num):
    users = ['dummydata101']
    userscores = []
    for i in range(num):
        charlen = random.randint(1,10)
        username = 'dummydata101'
        while username in users:
            charlen = random.randint(1,10)
            username = getchars(charlen)
        score = genscore()
        users.append(username)
        userscores.append([username, score])
    return userscores

# generates a username
def getchars(times):
    chars = ''
    # get first alphabet character
    char = random.randint(0, 51)
    chars += alphas[char]
    for i in range(times-1):
        char = random.randint(0, 61)
        chars += alphas[char]
    return chars

# generates a score
def genscore():
    score = random.randint(0, 99999)
    return score

# sorts the list of usernames and scores
def bubblesort(array):
    swaps = len(array) - 1
    while swaps != 0:
        for i in range(swaps):
            if array[i][1] < array[i+1][1]:
                array[i], array[i+1] = array[i+1], array[i]
            elif array[i][1] == array[i+1][1] and array[i][0] > array[i+1][0]:
                array[i], array[i+1] = array[i+1], array[i]
        swaps = swaps - 1
    return array

# open files for writing
outfile = open('HIGHSCORES.TXT', 'w')

allscores = genlist(5000)
allscores = bubblesort(allscores)
for element in allscores:
    outfile.write(element[0] + ", " + str(element[1]) + "\n")

outfile.close()
