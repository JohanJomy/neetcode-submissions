class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False
             
        hmap = defaultdict(int)

        for i in hand:
            hmap[i] +=  1

        minheap = list(hmap.keys())
        heapq.heapify(minheap)

        while minheap:
            n = minheap[0]
            for i in range(n, n + groupSize):
                if i not in hmap:
                    return False

                hmap[i] -= 1

                if hmap[i] == 0:
                    if i != minheap[0]:
                        return False

                    heapq.heappop(minheap)
        
        return True