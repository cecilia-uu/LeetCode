from collections import defaultdict

def solution(salesData, frequencyThreshold) -> int:
    l = 0
    n = len(salesData)
    frequency = defaultdict(int)
    ans = 0

    for r in range(n):
        frequency[salesData[r]] += 1

        while frequency[salesData[r]] > frequencyThreshold:
            frequency[salesData[l]] -= 1
            if frequency[salesData[l]] == 0:
                del frequency[salesData[l]]
            l += 1
        ans = max(ans, r - l + 1)
    
    return ans


salesData = [1, 2, 1, 3, 2]
frequencyThreshold = 1
print(solution(salesData, frequencyThreshold))
print(solution(salesData = [1,1,1,2,2,3,3,4,4,4], frequencyThreshold=2))