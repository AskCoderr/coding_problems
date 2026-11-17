length = input()
numbers = input()
li = numbers.split()
for i in li:
    temp = ""
    for k in range(1, int(i)+1):
        temp += bin(k)[2:]
    decimal = int(temp)
    print(decimal % 998244353)