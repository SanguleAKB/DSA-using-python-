import collections

q = collections.deque()


# implementation using append and popleft
q.append(10)
q.append(20)
q.append(30)
q.append(40)

q.popleft()

print("Front : ",q[-1])
print("Rear : ",q[0])
print(q)