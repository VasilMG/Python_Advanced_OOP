from  collections import deque
n, m = [int(x) for x in input().split()]

word = input()
text = deque([x for x in word])

mm = []
for row in range(n):
    if row % 2 == 0:
        the_row = []
        for column in range(m):
                if len(text) > 0:
                    the_row.append(text.popleft())
                else:
                    text = deque([x for x in word])
                    the_row.append(text.popleft())
    else:
        the_row = deque()
        for column in range(m):
            if len(text) > 0:
                the_row.appendleft(text.popleft())
            else:
                text = deque([x for x in word])
                the_row.appendleft(text.popleft())
    mm.append(the_row)

    
for r in mm:
    print("".join([x for x in r]))
