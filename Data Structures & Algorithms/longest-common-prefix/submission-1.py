class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        length = 0
        flag = 1
        while flag:
            if len(strs[0]) < length + 1:
                break

            c = strs[0][length]
            for i in range(1, len(strs)):
                if len(strs[i]) < length + 1 or strs[i][length] != c:
                    flag = 0
                    break
            else:
                length += 1
        
        # print(length)
        
        return strs[0][:length]