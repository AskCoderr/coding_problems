def count(string):
    di = {}
    for o in string:
        if o in di.keys():
            di[o] += 1
        else:
            di[o] = 1
    return di


# https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python
