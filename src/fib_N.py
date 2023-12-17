def fib_N(n: int) -> int:
    """
    Возвращает число Фибоначчи от n за O(n)
    """

    if n == 0:
        return 0

    first, second = 0, 1

    for _ in range(2, n):
        tmp = second
        second = first + second
        first = tmp

    return second
