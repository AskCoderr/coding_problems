import sys

input = sys.stdin.readline
out = []

num_testcases = int(input())

for i in range(num_testcases):
    testcase = int(input())
    
    if testcase < 3:
        out.append("light")
    elif 3 <= testcase < 7:
        out.append("moderate")
    else:
        out.append("heavy")
        
print("\n".join(out))
