a = [1, 2, 4, 5, 6, 78, 324, 345, 5, 432, 45, 23, 46, 13, 3, 4, 5, 6, 7, 8]

print(a[:6])
print(a[6:])


def f():
    return 10, 2, 3, 4


a = f()
if (isinstance(a, tuple)):
    print(a[0])
else:
    print(a)
