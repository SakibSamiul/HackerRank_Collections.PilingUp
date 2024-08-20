from collections import deque
T = int(input())
for n in range(T):
    n = input()
    blocks = deque(map(int, input().split()))

    for i in reversed(sorted(blocks)):
        if blocks[-1] == i:
            blocks.pop()
        elif blocks[0] == i:
            blocks.popleft()
        else:
            print("No")
            break
    else:
        print("Yes")

    
