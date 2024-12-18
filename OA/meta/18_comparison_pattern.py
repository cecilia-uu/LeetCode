def compare(p, numbers, i):
    if p == 1:
        return numbers[i+1] > numbers[i]
    elif p == 0:
        return numbers[i+1] == numbers[i]
    else:
        return numbers[i+1] < numbers[i]
    
def solution(numbers, pattern) -> int:
    p, n = len(pattern), len(numbers)
    ans = 0

    for i in range(n-p):
        match = True
        for j in range(p):
            match = compare(pattern[j], numbers, i+j)
            if match == False:
                break
        if match:    
            ans += 1
    return ans

print(solution([4,1,3,4,4,5,5,1], [1,0,-1]))