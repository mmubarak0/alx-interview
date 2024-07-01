#!/usr/bin/python3
"""To determine if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Determine if all the boxes can be opened."""
    from collections import deque

    # iter = 1
    stack = deque()
    visited = set()

    stack.append(boxes[0])
    visited.add(0)
    while stack:
        # print("=====================================")
        # print(f"iteration number: {iter}")
        # print(f"###########boxes: {boxes}#############")
        # print(f"stack: {list(stack)}")
        # print(f"visited: {visited}")
        # print("=====================================")
        # iter += 1
        box = stack.popleft()
        for key in box:
            if key < len(boxes) and key not in visited:
                stack.append(boxes[key])
                visited.add(key)
        if len(visited) == len(boxes):
            return True
    return False
