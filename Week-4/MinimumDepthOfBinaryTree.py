# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        que=collections.deque()
        if root:
            que.append((root,1))
            while que:
                current,depth=que.popleft()
                if not current.left and not current.right:
                    return depth
                if current.left:
                    que.append((current.left,depth+1))
                if current.right:
                    que.append((current.right,depth+1))
        return 0