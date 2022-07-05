from collections import deque

deque = deque(["123", "1234"])
deque.append("abc")

deque.append("de")
deque.append("fg")

print(deque)
print(deque.pop())
print(deque.popleft())
print(deque)
