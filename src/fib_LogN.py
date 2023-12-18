# from time import sleep


def mat_exp(A: list[list], n: int) -> list[list]:
    """
    Arguments:
        A: list[list] - 2x2 matrix
        n: int
        
    Returns:
        list[list]: A**n
    """
    M = [[1, 0], [0, 1]]

    while n != 0:
        a00, a01, a10, a11 = A[0][0], A[0][1], A[1][0], A[1][1]
        # sleep(10**-3)

        if n % 2 == 1:
            # M = M * A
            m00, m01, m10, m11 = M[0][0], M[0][1], M[1][0], M[1][1]

            M[0][0] = m00 * a00 + m01 * a10
            M[0][1] = m00 * a01 + m01 * a11
            M[1][0] = m10 * a00 + m11 * a10
            M[1][1] = m10 * a01 + m11 * a11

        # A = A * A
        A[0][0] = a00 * a00 + a01 * a10
        A[0][1] = a00 * a01 + a01 * a11
        A[1][0] = a10 * a00 + a11 * a10
        A[1][1] = a10 * a01 + a11 * a11

        n = n // 2

    return M


def fib_LogN(n: int) -> int:
    """
    Arguments:
        n: int >= 0

    Returns:
        int: n-th Fibonacci number in O(Log(n))
    """

    if n <= 1:
        return n

    M = [[1, 1], [1, 0]]
    res = mat_exp(M, n - 1)
    return res[0][0]
