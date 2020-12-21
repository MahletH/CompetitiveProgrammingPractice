"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root:
            path=0
            que=collections.deque()
            que.append((root,1))
            while que:
                node,cur=que.popleft()
                if path!=cur:
                    prev=None
                    path=cur
                node.next=prev
                prev=node
                if node.right:
                    que.append((node.right,cur+1))
                if node.left:
                    que.append((node.left,cur+1))
        return root
        