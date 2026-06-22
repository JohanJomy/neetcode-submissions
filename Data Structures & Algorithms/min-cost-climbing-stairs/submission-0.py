class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # last vals and final step
        a, b = cost[-1], 0

        for i in range(len(cost)-2, -1, -1):
            # cost from e = min()
            c = cost[i]
            # print(c, a, b)
            cost_to_last = min(c+a, c+b)
            b = a
            a = cost_to_last
        
        return min(a, b)
