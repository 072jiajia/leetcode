class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        MinLen = min([len(string) for string in strs])
        for i in range(MinLen):
            char = strs[0][i]
            for string in strs[1:]:
                if char != string[i]:
                    return strs[0][:i]
        return strs[0][:MinLen]
