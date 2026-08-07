class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # bills.sort()

        five, ten = 0, 0

        for i in bills:
            # print(i, five, ten)
            if i == 5:
                five += 1
            elif i == 10:
                ten += 1
                if five == 0:
                    return False
                five -= 1
            else:
                if ten > 0:
                    ten -= 1
                    if five > 0:
                        five -= 1
                    else:
                        return False
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True 