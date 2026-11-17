import re
import string


def pig_it(text):
    new_var = ""
    add_text = "ay"
    pattern = re.compile(r"\S")
    punc_pattern = re.compile(r"")
    strt_var = None
    end_var = None
    length = len(text)

    for i in enumerate(text):
        if i[1] in string.punctuation and strt_var == None:
            new_var += i[1]

        elif (bool(pattern.match(i[1]))) and ((i[0]+1) != length):
            if strt_var == None:
                strt_var = i[0]
                end_var = i[0]
            else:
                end_var = i[0]
        elif (bool(pattern.match(i[1])) == False) or ((i[0]+1) == length):
            if (i[0]+1) == length and i[1] != " ":
                if end_var == None:
                    new_var += f"{text[-1]}ay"
                else:
                    end_var += 1

            if strt_var != None:
                new_var += f"{text[(strt_var+1):(end_var+1)]}{text[strt_var]}{add_text}"
                if (i[0]+1) != length:
                    new_var += " "
                strt_var = None
                end_var = None
            else:
                new_var += " "

    return new_var


print(pig_it("Hello's world !"))

# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
