# from time import sleep
def fib_N(n: int) -> int:
    """
    Arguments:
        n: int >= 0

    Returns:
        int: n-th Fibonacci number in O(n)
    """

    if n == 0:
        return 0

    first, second = 0, 1

    for _ in range(1, n):
        # sleep(10**-3)
        tmp = second
        second = first + second
        first = tmp

    return second
