for x in range(1, 11):
    print(repr(x).rjust(2), repr(x ** 2).rjust(3), end=' ')
    print(repr(x ** 3).rjust(4))

print('12'.zfill(5))
