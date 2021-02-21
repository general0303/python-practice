def multiply12(x):
    x = x + x + x
    x = x + x
    x = x + x
    return x


def multiply16(x):
    x = x + x
    x = x + x
    x = x + x
    x = x + x
    return x


def multiply15(x):
    # в 3 сложения умножить на 15 невозможно, можно максимум только на 8
    y = x
    x = x + x
    x = x + x
    x = x + x
    x = x + x
    x = x - y
    return x


def multiply29(x):
    y = x
    x = x + x
    x = x + x + y
    x = x + x + x
    x = x + x
    x = x - y
    return x


def naive_mul(x, y):
    if x == 0 or y == 0:
        return 0
    r = x
    for i in range(0, y-1):
        x = x + r
    return x

print(multiply12(2))
print(multiply16(2))
print(multiply15(2))
print(multiply29(2))