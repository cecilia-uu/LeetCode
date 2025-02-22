# 103. Binary Tree Zigzag Level Order Traversal
# Medium
# Topics
# Companies
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
# (i.e., from left to right, then right to left for the next level and alternate between).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # first level is the root
        # second level is from the left to the right
        # then right to the left
        q = deque()
        direction = "right"
        q.append(root)

        res = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
            res.append(level)
            if direction == "right":
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                direction = "left"
            else:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                direction = "right"
        return res
