from .fib_LogN import fib_LogN
from .fib_N import fib_N


def fibonacci(n: int, a: str) -> int:
    """
    Arguments:
        n: int (0 <= n <= 500)
        a: str ("N", "logN")
    
    Returns:
        int: n-th Fibonacci number in O(n) or O(log(N)) based on the specified alghorithm (N or logN).
        Provides type and value checks of the inputs.
    """

    if type(n) is not int:
        raise TypeError(f"n is supposed to be int, but {type(n)} was given")
    if type(a) is not str:
        raise TypeError(f"a is supposed to be str, but {type(a)} was given")
    if n < 0 or n > 500:
        raise ValueError(f"n is not in range 0..500")
    if a not in ("N", "LogN"):
        raise ValueError(f"a is supposed to be either N or LogN, but {a} was given")

    if a == "N":
        return fib_N(n)
    elif a == "LogN":
        return fib_LogN(n)
