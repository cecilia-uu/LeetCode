# orchard - graph: "-" empty, "T" healthy tree, "R" rotten tree
# rot spread - 4 directions

import collections


def solution(orchard, days):
    rotten = collections.deque()
    m, n = len(orchard), len(orchard[0])
    for i in range(m):
        for j in range(n):
            if orchard[i][j] == "R":
                rotten.append((i, j))

    visited = set()
    while days and rotten:
        i, j = rotten.popleft()
        for x, y in [(1,0),(-1,0),(0,1),(0,-1)]:
            r, c = x + i, y+j
            if r in range(m) and c in range(n) and orchard[r][c] == "T" and (r,c) not in visited:
                visited.add((r,c))
                orchard[r][c] = "R"
                rotten.append((r,c))
        days -= 1
    return orchard

print(solution([
    ["T", "R", "-", "-"],
    ["-", "T", "T", "R"],
    ["T", "T", "-", "R"],
    ["-", "-", "R", "-"]
                ], 2))