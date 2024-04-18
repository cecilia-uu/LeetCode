"""
埃式筛
欧拉筛 线性筛
"""
# 暴力
from math import isqrt
class Solution:  
    # sqrt(100)
    def isPrime(self, n):
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
        return n >= 2
    # O(n)
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        i = 0
        while not self.isPrime(nums[i]):
            i += 1
        
        j = len(nums) - 1
        while not self.isPrime(nums[j]):
            j -= 1