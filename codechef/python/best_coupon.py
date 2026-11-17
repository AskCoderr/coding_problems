import sys

input = sys.stdin.readline
out = []

num_cases = int(input())

for _ in range(num_cases):
    price = int(input())
    disc = ((price*10)//100)
    
    if disc > 100:
        out.append(str(disc))
    else:
        out.append("100")
    
print("\n".join(out)) 