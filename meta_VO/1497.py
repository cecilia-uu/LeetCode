# 1497. Check If Array Pairs Are Divisible by k
# Medium
# Topics
# Companies
# Hint
# Given an array of integers arr of even length n and an integer k.

# We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

# Return true If you can find a way to do that or false otherwise.

 

# Example 1:

# Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# Output: true
# Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
# Example 2:

# Input: arr = [1,2,3,4,5,6], k = 7
# Output: true
# Explanation: Pairs are (1,6),(2,5) and(3,4).
# Example 3:

# Input: arr = [1,2,3,4,5,6], k = 10
# Output: false
# Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
 

# Constraints:

# arr.length == n
# 1 <= n <= 105
# n is even.
# -109 <= arr[i] <= 109
# 1 <= k <= 105

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if sum(arr) % k: return False
        # {mod: number} (new_mod + mod) % mod = 0
        mod_mapping = set()
        for n in arr:
            new_mod = n % k
            if k - new_mod in mod_mapping:
                mod_mapping.remove(k-new_mod)
            else:
                mod_mapping.add(new_mod)
        return mod_mapping is None