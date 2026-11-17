def zeroes(n):
    x = 0
    y = 5
    while n // y > 0:
        x += n // y
        y *= 5
    return x

print(zeroes(1000000000))

# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/python
# kinda did not do by my own

    # for i in range(2, n+1):
    #     x = 1
    #     while i % 2**x == 0:
    #         no_of_2 += 1
    #         x += 1
    #     x = 1
    #     while i % 5**x == 0:
    #         no_of_5 += 1
    #         x += 1
        
    # return min(no_of_2, no_of_5)
