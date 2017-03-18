__author__ = 'minin'


def super_fibonacci(n, m):
    if (n == 1) | ((n == 2) & ( m == 1 )):
        return 1

    fibonacci = []
    for i in range(n):
        if i < m:
            fibonacci.append(1)
        else:
            sum = 0
            for i in fibonacci[-m:]:
                sum += i
            fibonacci.append(sum)
    return fibonacci[n - 1]


print super_fibonacci(3, 5)