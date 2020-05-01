date = input("Enter the date like dd.mm.yyyy: ")
date_int = date.split('.')
day = str(date_int[0])
month = str(date_int[1])
year = str(date_int[2])

days = {
    '0': 'lol',
    '01': 'first',
    '02': 'second',
    '03': 'third',
    '04': 'fourth',
    '05': 'fifth',
    '06': 'sixth',
    '07': 'seventh',
    '08': 'eighth',
    '09': 'ninth',
    '10': 'tenth',
    '11': 'eleventh',
    '12': 'twelfth',
    '13': 'thirteenth',
    '14': 'fourteenth',
    '15': 'fifteenth',
    '16': 'sixteenth',
    '17': 'seventeenth',
    '18': 'eighteenth',
    '19': 'nineteenth',
    '20': 'twentieth',
    '21': 'twentieth first',
    '22': 'twentieth second',
    '23': 'twentieth third',
    '24': 'twentieth fourth',
    '25': 'twentieth fifth',
    '26': 'twentieth sixth',
    '27': 'twentieth seventh',
    '28': 'twentieth eighth',
    '29': 'twentieth nineteenth',
    '30': 'thirtieth',
    '31': 'thirtieth first'
}

months = {
    '0': 'lol',
    '01': 'january',
    '02': 'february',
    '03': 'march',
    '04': 'april',
    '05': 'may',
    '06': 'june',
    '07': 'july',
    '08': 'august',
    '09': 'september',
    '10': 'october',
    '11': 'november',
    '12': 'december',
}

print('The date is the {} {} of {}'.format(days[day], months[month], year))