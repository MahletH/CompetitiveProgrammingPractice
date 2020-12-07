class Solution:
    def minFlips(self, target: str) -> int:
        move=0
        prev="0"
        for num in target:
            if prev!=num:
                move+=1
                prev=num
        return move
