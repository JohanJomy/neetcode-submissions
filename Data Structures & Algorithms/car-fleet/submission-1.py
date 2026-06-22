class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        ps = [[position[i], speed[i]] for i in range(len(position))]

        ps.sort(reverse=True)

        stack = []
        # print(ps)
        for p, s in ps:
            t = (target - p) / s
            print(t)
            if not stack or stack[-1] < t:
                stack.append(t)
        
        return len(stack)
