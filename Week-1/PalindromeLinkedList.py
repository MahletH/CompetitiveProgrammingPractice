# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        inputList=[]
        start= head
        while start:
            inputList.append(start.val)
            start=start.next
        for i in range(len(inputList)//2):
            if inputList[i] != inputList[len(inputList)-1-i]:
                return False
        return True
