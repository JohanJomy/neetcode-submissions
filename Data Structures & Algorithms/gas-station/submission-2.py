class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        res = 0
        balance = 0
        for i in range(len(gas)):
            balance += gas[i] - cost[i]

            if balance < 0:
                res = i+1
                balance = 0

        return res