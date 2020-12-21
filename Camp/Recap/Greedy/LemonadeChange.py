class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_of_five, count_of_ten = 0, 0
        for bill in bills:
            if bill==5:
                count_of_five+=1
            elif bill==10:
                if not count_of_five:
                    return False
                count_of_ten+=1
                count_of_five-=1
            else:
                if not count_of_five:
                    return False
                if count_of_ten:
                    count_of_ten-=1
                    count_of_five-=1
                else:
                    if count_of_five<3:
                        return False
                    count_of_five-=3
        return True