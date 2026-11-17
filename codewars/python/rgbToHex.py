def rgb(r, g, b):
    li = [r, g, b]
    for i in enumerate(li):
        if i[1] > 255:
            li[i[0]] = 255
        elif i[1] < 0:
            li[i[0]] = 0
    string = ""
    for i in li:
        hexa = hex(i)[2:].upper()
        if len(hexa) == 1:
            hexa = f"0{hexa}"
        string += hexa
    return string


print(rgb(255, 255, 300))
# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
