# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.elements=[float('-inf')]
        visited=set()
        stack=[root]
        while root.left:
            stack.append(root.left)
            root=root.left
        while stack:
            cur=stack.pop()
            self.elements.append(cur.val)
            if cur.right:
                stack.append(cur.right)
                cur=cur.right
                while cur.left:
                    stack.append(cur.left)
                    cur=cur.left
        self.ptr=0
    def next(self) -> int:
        self.ptr+=1
        return self.elements[self.ptr]
    def hasNext(self) -> bool:
        return self.ptr<len(self.elements)-1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()