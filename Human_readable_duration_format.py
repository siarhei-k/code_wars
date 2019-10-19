'''
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
'''

def format_duration(seconds):
    year = seconds // 31536000
    day = seconds % 31536000 // 86400
    hour = seconds % 31536000 % 86400 // 3600
    minute = seconds % 31536000 % 86400 % 3600 // 60
    sec = seconds % 31536000 % 86400 % 3600 % 60

    frz = []

    if year != 0:
        if year == 1:
             frz.append(str(year) + ' year')
        else:
            frz.append(str(year) + ' years')

    if day != 0:
        if day == 1:
             frz.append(str(day) + ' day')
        else:
            frz.append(str(day) + ' days')

    if hour != 0:
        if hour == 1:
             frz.append(str(hour) + ' hour')
        else:
            frz.append(str(hour) + ' hours')

    if minute != 0:
        if minute == 1:
             frz.append(str(minute) + ' minute')
        else:
            frz.append(str(minute) + ' minutes')

    if sec != 0:
        if sec == 1:
             frz.append(str(sec) + ' second')
        else:
            frz.append(str(sec) + ' seconds')

    if len(frz) == 1:
        return(''.join(frz))
    elif len(frz) == 0:
        return('now')
    else:
        return(', '.join(frz[0:-1]) + ' and ' + frz[-1])

