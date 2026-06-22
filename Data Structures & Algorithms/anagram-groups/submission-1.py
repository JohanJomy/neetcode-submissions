class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            sorted_str = ''.join(sorted(s))
            hashmap[sorted_str] = hashmap.get(sorted_str, []) + [s]
        
        return list(hashmap.values())