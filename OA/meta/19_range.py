def solution(left, right) -> int:
    res = 0
    for n in range(left, right+1):
        s = str(n)
        if s[0] != s[1] and s[1] != s[2] and s[0] != s[2]:
            res += 1
    return res

print(solution(876, 890))