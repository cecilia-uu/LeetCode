# centers - side=2
# calculate the number of object pairs that collide

import math
def length(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

def solution(centers) -> int:
    n = len(centers)
    ans = 0

    for i in range(n):
        for j in range(i+1,n):
            if length(centers[i], centers[j]) <= 8:
                ans += 1
    return ans

print(solution([[1, 1], [3, 3], [2, 2], [5, 5]]))