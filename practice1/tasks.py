import math


def task11(x, y):
    return (32 * y ** 6 - 90 * y) / (math.sin(78 * y ** 7 + y ** 2) - math.cos(y)) - math.sqrt(
        (x ** 4 - y ** 2 - 23) / x ** 7 +
        math.log(x)) - math.sqrt((math.tan(x) + x ** 8) / (y ** 2 + 58 * y ** 3))


def task12(x):
    if x < 72:
        return 32 * (x ** 7 + 23 * x ** 3) ** 6 - 59 * x
    elif x < 117:
        return 77 * (x - x ** 2) - 51 * x ** 5
    elif x < 208:
        return math.cos(47 * x ** 7 + math.cos(x)) + math.fabs(x ** 3 + 53 * x ** 4)
    else:
        return math.sin(56 * x ** 7) - x / 90 - 29


def task13(n, m):
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sum += 32*j**2 - 90 * j ** 7
    for i in range(1, n + 1):
        for i in range(1, m + 1):
            sum += 77 * (math.tan(j) + 59 * j + 5)
    return sum


def task14(n):
    if n == 0:
        return 7
    elif n == 1:
        return 9
    else:
        return math.tan(task14(n - 2)) + math.fabs(task14(n-1))


print("{:.2e}".format(task11(79, 35)))
print("{:.2e}".format(task12(192)))
print("{:.2e}".format(task13(86, 95)))
print("{:.2e}".format(task14(8)))
