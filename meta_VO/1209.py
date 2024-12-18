# 1209. Remove All Adjacent Duplicates in String II
# Medium
# Topics
# Companies
# Hint
# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent 
# and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

# Example 1:

# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.
# Example 2:

# Input: s = "deeedbbcccbdaa", k = 3 [d,e,e] e
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"
# Example 3:

# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"
 

# Constraints:

# 1 <= s.length <= 105
# 2 <= k <= 104
# s only contains lowercase English letters.
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            elif len(stack) >= k - 1 and all(stack[-(k-1):]) == c:
                for _ in range(k-1):
                    stack.pop()
            else:
                stack.append(c)
        return "".join(stack)