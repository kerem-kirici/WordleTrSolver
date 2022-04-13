
from collections import defaultdict
from math import log


with open('.\\words_tr.txt', 'r', encoding='utf-8') as file:
    words = file.read().split()

info_text = '''
This code is written by Kerem Kırıcı

Program uses information theory to guess the answer.

The first guess may take about 30 seconds to compute so you may need to wait for it thanks for your patience.
                                            (special thanks to 3Blue1Brown)


  Program Info:

    First, program gives you a sorted list(length:10) of guesses from best to worst. (Starts with the word 'Serak')

    After you pick you guess and write it to the Wordle Tr game you write here game's output (space sperated) where:
      * 0 - for Black
      * 1 - for Yellow
      * 2 - for Green
    and the game continues with next guesses...


    Example: 
      Hidden Word -> süper

      Best Options: ['serak', 'merak', 'kelam', 'tarik', 'kamer', 'kalem', 'kemal', 'kenar', 'ketal', 'keman']
      Your Guess: serak
      Output: 2 1 1 0 0

      Best Options: ['süper', 'siper', 'sümer', 'siyer', 'sütre', 'sperm']
      Your Guess: süper
      Output: 2 2 2 2 2

'''
print(info_text)

def word_outcome(word1, word2):
    out = [0, 0, 0, 0, 0]
    for i in range(5):
        if word1[i] == word2[i]:
            out[i] = 2
            word1 = word1[:i] + str(i) + word1[i+1:]
            word2 = word2[:i] + str(9-i) + word2[i+1:]
    for i in range(5):
        if word2[i] in word1:
            out[i] = 1
    return tuple(out)

def play():
    global words
    outcome = None
    guessed = None
    while outcome != (2, 2, 2, 2, 2):
        if outcome is not None:
            new_words = []
            for w in words:
                if word_outcome(w, guessed) == outcome:
                    new_words.append(w)
            words = new_words.copy()
        print('\nComputing Guesses...')
        g = guess()
        print('Best Options:', g[:10])
        guessed = input('Your Guess: ').lower()
        outcome = tuple(map(int, input('Outcome: ').split()))


def guess():
    global words
    word_entropies = defaultdict(float)

    for w1 in words:
        outcomes = defaultdict(int)
        for w2 in words:
            outcomes[word_outcome(w1, w2)] += 1

        for k in outcomes.values():
            p = k/len(words)
            word_entropies[w1] += -p*log(p,2)

    return sorted(word_entropies.keys(), key=lambda x: word_entropies[x], reverse=True)


play()
