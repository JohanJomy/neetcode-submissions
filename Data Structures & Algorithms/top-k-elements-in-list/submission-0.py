class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for i in nums:
            hashmap[i] += 1
        print(hashmap)

        length_list = [[] for i in range(len(nums))]

        for i in hashmap:
            length_list[hashmap[i] - 1].append(i)
        
        result = []
        for i in range(len(length_list)-1, -1, -1):
            result.extend(length_list[i])
            if len(result) == k:
                return result
