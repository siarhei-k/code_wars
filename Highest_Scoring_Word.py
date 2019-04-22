'''
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''

def high(x):
    t = 0
    i = 0
    abc = 'abcdefghijklmnopqrstuvwxyz'
    max_count = 0
    words = x.split(' ')
    for i in words:
        count = 0
        for t in range(len(i)):
            count += (abc.index(i[t]) + 1)
        if count > max_count:
            max_count = count
            max_word = i


    return max_word

print(high('take me to semynak'))
