# n, m = map(int, input().split())

# red_balls = []
# for i in range(1, n+1):
#     xi, ui = map(int, input().split())
#     red_balls[i] = (xi, ui)

# blue_balls = []
# for i in range(1, m+1):
#     yi, vi = map(int, input().split())
#     blue_balls[i] = (yi, vi)
    
import random
import time

n = 10000
m = 10000

red_balls = {i: (random.randint(1, 10**6), random.randint(1, 1000)) for i in range(1, n + 1)}
blue_balls = {i: (random.randint(1, 10**6), random.randint(1, 1000)) for i in range(1, m + 1)}
    
start_time = time.time()
total_collision = 0

for i in range(1, n+1):
    for k in range(1, m+1):
        if blue_balls[k] == None:
            continue
        collision_time_r = blue_balls[k][0]/red_balls[i][1]
        collision_time_b = red_balls[i][0]/blue_balls[k][1]
        if collision_time_r == collision_time_b:
            red_balls[i] = None
            blue_balls[k] = None
            total_collision += 1
            break
        

print(total_collision)
print("Execution time:", time.time() - start_time, "seconds")