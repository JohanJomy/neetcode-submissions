class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        prices = [float('inf')] * n # prices (min) to reach to that node

        prices[src] = 0

        for i in range(k+1):
            temp_prices = prices.copy()
            for f, t, p in flights:
                if prices[f] == float('inf'):
                    continue
                
                temp_prices[t] = min(temp_prices[t], prices[f] + p)
            # print(temp_prices)
            prices = temp_prices.copy()

        if prices[dst] == float('inf'):
            return -1
        
        return prices[dst]

