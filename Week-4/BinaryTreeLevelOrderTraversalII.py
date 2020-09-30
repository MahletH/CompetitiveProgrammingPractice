# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        top_down_list, stack = [], [(root, 0)]
        while stack:
            node, level = stack.pop()
            if node:
                if level == len(top_down_list):
                    top_down_list.append([])
                top_down_list[level].append(node.val)
                stack.append((node.right, level + 1))
                stack.append((node.left, level + 1))
        return reversed(top_down_list)