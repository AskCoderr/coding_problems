def count_zeros_n_double_fact(n):
    num_of_zeros = 0
    acc = 1
    if n % 2 == 0:
        strt_var = 2
        while strt_var <= n:
            acc *= strt_var
            strt_var += 2
    else:
        strt_var = 1
        while strt_var <= n:
            acc *= strt_var
            strt_var += 2

    string = str(acc)
    while string[-1] == "0":
        num_of_zeros += 1
        string = string[0:-1]
    return num_of_zeros


print(count_zeros_n_double_fact(30))
#https://www.codewars.com/kata/58cbfe2516341cce1e000001/train/python
