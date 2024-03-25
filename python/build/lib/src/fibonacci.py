def strassen_mult(x: list[list[int]], y: list[list[int]]) -> list[list[int]]:
    p1 = x[0][0] * (y[0][1] - y[1][1])
    p2 = (x[0][0] + x[0][1]) * y[1][1]
    p3 = (x[1][0] + x[1][1]) * y[0][0]
    p4 = x[1][1] * (y[1][0] - y[0][0])
    p5 = (x[0][0] + x[1][1]) * (y[0][0] + y[1][1])
    p6 = (x[0][1] - x[1][1]) * (y[1][0] + y[1][1])
    p7 = (x[0][0] - x[1][0]) * (y[0][0] + y[0][1])

    result = [[0, 0], [0, 0]]
    result[0][0] = p5 + p4 - p2 + p6
    result[0][1] = p1 + p2
    result[1][0] = p3 + p4
    result[1][1] = p1 + p5 - p3 - p7
    return result


def matrix_exp(m, n):
    if n % 2 == 1:
        if (n == 1):
            return m
        return strassen_mult(matrix_exp(m, n-1), m)
    matrix_half = matrix_exp(m, n/2)
    return strassen_mult(matrix_half, matrix_half)


def fib(n):
    m = [[1, 1], [1, 0]]
    m = matrix_exp(m, n)
    return m[0][1]
