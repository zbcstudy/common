from math import pi

squares = list(map(lambda x: x ** 2, range(10)))

print(squares)
print(map(lambda x: x ** 2, range(10)))

squares2 = [x ** 2 for x in range(10)]
print(squares2)

s = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(s)

vec = [-4, -2, 0, 2, 4]
print([x * 2 for x in vec])
print([x * 2 for x in vec if x >= 0])

print([abs(x) for x in vec])

# two
vec2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for nums in vec2 for num in nums])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 复杂的列表推导式
print([str(round(pi, i)) for i in range(1, 6)])

# 嵌套列表推导式
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])

# 等价于
print(list(zip(*matrix)))

print(zip(*matrix))
