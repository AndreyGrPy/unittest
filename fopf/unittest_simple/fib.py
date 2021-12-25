def fib(n):
    if not isinstance(n, int):
        raise TypeError("Fibonacci function can work with only class <int> type.")
    if n < 0:
        raise ValueError("Fibonacci can't work with negative numbers.")
    if n >= 10000:
        raise ValueError("Fibonacci can't work with numbers large than 9999.")
    F = [0, 1] + [0]*(n - 1)
    for i in range(2, n + 1):
        F[i] = F[i-1] + F[i-2]
        return F[n]


if __name__ == "__main__":
    import doctest
    doctest.testmod()