def solution(args):
    new_str = ""
    init = None
    final = None
    length = len(args)
    for i in range(length-1):
        if i == length-2:
            if args[-1]-args[-2] == 1:
                if init != None:
                    final = args[-1]
                    new_str += f"{init}-{final}"
                else:
                    new_str += f"{args[-2]},{args[-1]}"
            else:
                if init != None and final-init >= 2:
                    new_str += f"{init}-{final},{args[-1]}"
                elif init != None:
                    new_str += f"{args[-3]},{args[-2]},{args[-1]}"
                else:
                    new_str += f"{args[-2]},{args[-1]}"
        elif args[i+1]-args[i] == 1:
            final = args[i+1]
            if init == None:
                init = args[i]
        else:
            if init != None and final-init >= 2:
                new_str += f"{init}-{final},"
                init, final = None, None
            elif init != None:
                new_str += str(args[i-1])+","
                new_str += str(args[i])+","
                init, final = None, None
            else:
                new_str += str(args[i])+","

    return new_str


print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5,
      7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))

# dont think i did it in an efficient and effective way
#expected - '-6,-3-1,3-5,7-11,14,15,17-20'
# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/python
