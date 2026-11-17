def bouncing_ball(h, bounce, window):
    if h > 0 and 0 < bounce < 1 and window < h:
        count = -1
        while h > window:
            count += 2
            h *= bounce
        return count
    else:
        return -1


print(bouncing_ball(3, 0.66, 1.5))

# https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python
