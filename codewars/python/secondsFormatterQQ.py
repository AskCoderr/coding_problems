import re


def format_duration(seconds):
    if seconds == 0:
        return 'now'
    div_by = (60, 60, 24, 365)
    split_data = [seconds]
    i = 0
    while i <= 3:
        quotient = split_data[i] // div_by[i]
        remainder = split_data[i] % div_by[i]
        if quotient >= 1:
            split_data.append(quotient)
            split_data[i] = remainder
        else:
            break
        i += 1

    units = ('second', 'minute', 'hour', 'day', 'year')
    for i in range(len(split_data)):
        unit = units[i]
        if split_data[i] > 1:
            unit += 's'
        split_data[i] = f'{split_data[i]} {unit}'

    string = ''
    for k in split_data[:0:-1]:
        string += f'{k}, '
    if len(string):
        string = string[:-2] + ' '
        if split_data[0] != '0 second':
            string += f'and {split_data[0]}'
    else:
        string = split_data[0]

    pattern = r' 0 .+'
    matched = re.search(pattern, string)
    print(matched)
    while matched:
        string = string.replace(matched.group(0), '')
        matched = re.search(pattern, string)

    return string


print(format_duration(2434))

# does the job but not in the perfect format therefore test not passed
# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python
