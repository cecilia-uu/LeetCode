def solution(a, b):
    n = len(a)
    res = 0
    for i in range(n):
        for j in range(i, n):
            if a[i] - b[j] == a[j] - b[i]:
                res += 1
    return res

print(solution([2,-2,5,3], [1,5,-1,1]))
print(solution([25,0], [0,25]))