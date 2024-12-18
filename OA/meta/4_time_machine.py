# time machine

def solution(years) -> int:
    ans = 0
    n = len(years)
    for i in range(1, n):
        if years[i] == years[i-1]:
            continue
        elif years[i] > years[i-1]:
            ans += 1
        else:
            ans += 2
    return ans

print(solution([2000,1990,2005,2050]))