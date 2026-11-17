def to_weird_case(words):
    active = True
    new_str = ""
    for i in words:
        if i == " ":
            active = False
            new_str += " "
        elif active:
            new_str += i.upper()
        else:
            new_str += i.lower()
        active = not active
    return new_str


print(to_weird_case("its a fun day"))

# https://www.codewars.com/kata/52b757663a95b11b3d00062d/train/python
