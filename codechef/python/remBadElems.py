import sys

input = sys.stdin.readline
out = []

num_cases = int(input())

for _ in range(num_cases):
    length = int(input())
    array = list(map(int, input().split()))
    data = {}
    for i in array:
        if i in data:
            data[i] += 1
        else:
            data[i] = 1
    maxx = 0
    for key in data:
        if data[key] > maxx:
            maxx = data[key]
            
    out.append(str(length-maxx))
    
print("\n".join(out))

# https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/REMOVEBAD
