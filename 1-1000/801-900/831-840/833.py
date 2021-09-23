class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        src_tgt_dict = {}
        for i in range(len(indices)):
            src_tgt_dict[indices[i]] = (sources[i], targets[i])

        ans = ""
        i = 0
        while i < len(s):
            if i not in src_tgt_dict:
                ans += s[i]
                i += 1
            else:
                source, target = src_tgt_dict[i]
                part = s[i : i + len(source)]
                if part == source:
                    ans += target
                else:
                    ans += part
                i += len(source)
        return ans
