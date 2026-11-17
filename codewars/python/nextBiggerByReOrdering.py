def next_bigger(n):
    li = list(str(n))
    li2 = []
    temp = -1
    for i in enumerate(li[-2::-1]):
        li2 = li[temp:]
        li2.sort()
        for u in enumerate(li2):
            if u[1] > i[1]:
                li2[u[0]], li[-2-i[0]] = li[-2-i[0]], li2[u[0]]
                li[temp:] = li2
                new_str = ""
                for i in li:
                    new_str += str(i)
                return int(new_str)
        temp -= 1
    return -1

num = int(input("Enter your number: "))
result = lambda x : "number not existent" if x == -1 else x
print(f"{num} -> {result(next_bigger(num))}")

# https://www.codewars.com/kata/55983863da40caa2c900004e/train/python
