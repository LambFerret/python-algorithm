
# 1. here`s your change
def change_counter(money):
    ls = [500, 100, 50, 10]
    count = 0
    for a in ls:
        b = money//a
        count += b
        money -= b*a
    return count


# print(change_counter(1260))


# 2. law`s of BIG NUMBER
def big_number(N, M, K):
    N = sorted(N,reverse=True)
    first, second = N[0], N[1]
    leave = M%(K+1)
    times = M//(K+1)
    number = (first*K+second)*times + leave*first
    return number


# print(big_number([2,4,5,4,6],8,3))
