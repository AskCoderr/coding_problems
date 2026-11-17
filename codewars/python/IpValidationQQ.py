import re


def is_valid_IP(strng):
    new_str = ""
    count = 0
    count_2 = 0
    pattern = re.compile(r"[0-9]")
    for i in strng:
        if i == ".":
            if new_str == "":
                return False
            elif (new_str[0] != "0") and (0 <= int(new_str) <= 255):
                count += 1
                count_2 += 1
                new_str = ""
            else:
                return False

        elif pattern.match(i) == None:
            return False

        else:
            new_str += i
            count_2 += 1

        if count_2 == len(strng):
            if new_str == "":
                return False
            elif (new_str[0] != "0") and (0 <= int(new_str) <= 255):
                count += 1
                count_2 += 1
                new_str = ""
            else:
                return False

    if count == 4:
        return True
    else:
        return False


print(is_valid_IP('123.045.067.089'))
# https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python