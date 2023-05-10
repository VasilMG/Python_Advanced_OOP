from collections import deque
people = input().split()
people = deque(people)
n = int(input())
toss = 1

while len(people) > 1:
    kid = people.popleft()
    if toss == n:
        print(f"Removed {kid}" )
        toss = 1
    else:
        toss += 1
        people.append(kid)

print(f"Last is {people.popleft()}")
