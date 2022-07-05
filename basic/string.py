print("-".join(['a', 'b', 'c']))

print("abc".upper())


def upper(word: str) -> str:
    w_list = []
    for w in word:
        if 'a' <= w <= 'z':
            w_list.append(chr(ord(w) - 32))
        else:
            w_list.append(w)
    return "".join(w_list)


# (chr(ord(char) - 32) if "a" <= char <= "z" else char for char in word)
def upper_up(word: str) -> list:
    res = []
    for char in word:
        res.append(chr(ord(char) - 32) if "a" <= char <= "z" else char)
    return res


print(upper("zbc"))
print(''.join(upper_up("zbc")))

print("zbc".center(12, "*"))

print("py" in "python")

year = 2021
event = 'Referendum'
print(f'Results of the {year} {event}')
print('1+1={}'.format(1 + 1))
print(repr(event))
