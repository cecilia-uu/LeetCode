# moniter energy usage
# grid

# readings: [int]
# k: int

def solution(readings, k) -> int:
    res = 0
    cur_k = 1  # Start with k^0 = 1 (first power of k)
    
    readings.sort()  # Sort the readings to iterate in increasing order
    
    for r in readings:
        # Compare the reading with powers of k until we surpass the current reading
        while cur_k < r:
            cur_k *= k
        # If a reading matches a power of k, increment the result
        if cur_k == r:
            res += 1
    
    return res

print(solution([2, 4, 7, 8, 16, 32, 120], 2))  # Output should be 5
print(solution([10201,101,1030301,101,101], 101)) # 5
# T: NlogN