def get_pins(observed):
    def adjacent(num):
        li = []
        var = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9],
               ["", 0, ""]]
        if num != 0:
            num_pos1 = ((num+2)//3)-1
        else:
            return [8]
        num_pos2 = var[num_pos1].index(num)
        if 0 < num_pos1:
            li.extend([str(var[num_pos1+1][num_pos2]),
                      str(var[num_pos1-1][num_pos2])])
        else:
            li.append(str(var[num_pos1+1][num_pos2]))
        if num_pos2 == 1:
            li.extend([str(var[num_pos1][num_pos2+1]),
                      str(var[num_pos1][num_pos2-1])])
        else:
            li.append(str(var[num_pos1][1]))

        for i in enumerate(li):
            if i[1] == "":
                li.pop(i[0])

        return li



print(get_pins(11))

# not completed
# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python
# ["11", "22", "44", "12", "21", "14", "41", "24", "42"]
