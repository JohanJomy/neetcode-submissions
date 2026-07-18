class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False
             
        hmap = Counter(hand)

        minheap = list(hmap.keys())
        heapq.heapify(minheap)

        while minheap:
            n = minheap[0]
            for i in range(n, n + groupSize):
                if i not in hmap or hmap[i] == 0:
                    return False

                hmap[i] -= 1

                if hmap[i] == 0:
                    if i != minheap[0]:
                        return False

                    heapq.heappop(minheap)
        
        return True