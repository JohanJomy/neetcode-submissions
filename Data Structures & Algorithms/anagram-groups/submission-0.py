class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            shashmap = [0] * 26

            for e in s:
                index = ord(e) - ord('a')
                shashmap[index] += 1
            
            shashmap = tuple(shashmap)
            print(shashmap)
            hashmap[shashmap] = hashmap.get(shashmap, []) + [s]
        
        return list(hashmap.values())