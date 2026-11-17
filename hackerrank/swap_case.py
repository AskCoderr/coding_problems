def swap_case(s):
    new_str = ""
    for i in s:
        if i.islower():
            new_str += i.upper()
        elif i.isupper():
            new_str += i.lower()
        else:
            new_str += i
    return new_str