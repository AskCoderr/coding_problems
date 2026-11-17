def parse_int(string):
    if string == "one million":
        return 1000000
    elif string == "zero":
        return 0
    while " and " in string:
        string = string.replace(" and ", " ")
    if string[-8:] == "thousand" or string[-8:] == " hundred":
        string += " "
    num = ""
    dict1 = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    dict2 = {
        "ten": 10,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90
    }
    dict3 = {
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19
    }

    check = ((dict1.keys()), (dict2.keys()), (dict3.keys()))
    stateThou = False
    stateHun = False
    if " thousand " in string:
        string = string.replace(" thousand ", "!")
        temp = string.split("!")
        if temp[1] == "":
            temp.pop(1)
        if temp[0].endswith("hundred"):
            temp[0] += " "
        stateThou = True
    else:
        temp = [string]
    for i in range(len(temp)):
        if " hundred " in temp[i]:
            temp[i] = temp[i].replace(" hundred ", "!")
            temp2 = temp[i].split("!")
            if temp2[1] == "":
                temp2.pop(1)
            stateHun = True
        else:
            temp2 = [temp[i]]
        for k in range(len(temp2)):
            if temp2[k] in check[1] or "-" in temp2[k] or temp2[k] in check[2]:
                if "-" in temp2[k]:
                    temp2[k] = temp2[k].replace("-", "!")
                    temp3 = temp2[k].split("!")
                    for j in range(2):
                        if temp3[j] in check[1]:
                            num += str(int(dict2[temp3[j]]/10))
                        elif temp3[j] in check[0]:
                            num += str(dict1[temp3[j]])
                elif temp2[k] in check[2]:
                    num += str(dict3[temp2[k]])
                else:
                    num += str(dict2[temp2[k]])
            elif temp2[k] in check[0]:
                num += str(dict1[temp2[k]])
            if stateHun and k == 0:
                if len(temp2) > 1 and temp2[1] in check[0]:
                    num += "0"
                elif len(temp2) == 1:
                    num += "00"
                stateHun = not stateHun

        if stateThou and i == 0:
            if len(temp) > 1 and temp[1] in check[0]:
                num += "00"
            elif len(temp) > 1 and "hundred" not in temp[1]:
                num += "0"
            elif len(temp) == 1:
                num += "000"
            stateThou = not stateThou

    try:
        return int(num)
    except ValueError:
        return num


print(parse_int(input("number: ")))
# https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5/train/python
# use '-' in between tenth numbers for proper functioning and specify the number in letters in proper format
