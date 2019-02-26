def count(n):
    memo = [0] * (n + 1)
    memo[0] = 1

    for i in range(1, n + 1):
        single = memo[i - 1]
        double = 0 if i - 2 < 0 else memo[i - 2]
        triple = 0 if i - 3 < 0 else memo[i - 3]

        memo[i] = single + double + triple

    return memo[n]

def top_down(n):
    memo = [-1] * (n + 1)
    memo[0] = 1

    return count_top_down(n, memo)

def count_top_down(n, memo):
    if n < 0:
        return 0

    if memo[n] > -1:
        return memo[n]

    return count_top_down(n - 1, memo) + count_top_down(n - 2, memo) + count_top_down(n - 3, memo)

def count_opt(n):
    if n == 0:
        return 1

    single = 1
    double = 0
    triple = 0
    current = 0

    for i in range(1, n + 1):
        current = single + double + triple
        triple = double
        double = single
        single = current

    return current
