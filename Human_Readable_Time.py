'''
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
'''

def make_readable(seconds):
    seq = seconds % 60

    min = seconds // 60
    while min >= 60:
        min = min - 60

    hr = seconds // (60 * 60)


    if seq <= 9:
        seq = str('0' + str(seq))

    if min == 60:
        min = 0
    if min <= 9:
        min = str('0' + str(min))


    if hr <= 9:
        hr = str('0' + str(hr))

    return (str(hr)+':'+str(min)+':'+str(seq))