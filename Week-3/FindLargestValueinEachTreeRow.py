#Leetcode link https://leetcode.com/problems/find-largest-value-in-each-tree-row


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def largestValues(self, root):
        if not root:
            return []
        queue = deque([root])
        largst_values = []
        while queue:
            current_max = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                current_max = max(current_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            largst_values.append(current_max)
        return largst_values  