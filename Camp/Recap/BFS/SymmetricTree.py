# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        que=collections.deque()
        que.append((root,root))
        while que:
            cur=que.popleft()
            if cur[0] and cur[1]:
                if cur[0].val==cur[1].val:
                    que.append((cur[0].left,cur[1].right))
                    que.append((cur[0].right,cur[1].left))
                else:
                    return False
            elif cur[0] or cur[1]:
                return False
        return True
            