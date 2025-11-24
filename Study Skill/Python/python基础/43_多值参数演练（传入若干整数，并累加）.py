def sums(*args):
    num_sums = 0
    for i in args:
        num_sums += i
    return num_sums


print(sums(1, 2, 3, 4, 5, 6))
