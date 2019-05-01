'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !!!
'''

def pig_it(text):
    a = text.split(' ')
    for i in range(len(a)):
       a[i] = a[i][1:] + a[i][0]
       if a[i] not in '!?':
           a[i] = a[i] + 'ay'
    return ' '.join(a)

print(pig_it('Pig latin is cool ?'))
