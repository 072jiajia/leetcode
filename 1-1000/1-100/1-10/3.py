class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_pos = {}
        last_i = 0
        max_len = 0
        for i, c in enumerate(s):
            if c in char_pos:
                move_pos = char_pos[c] + 1
                if move_pos > last_i:
                    max_len = max(max_len, i - last_i)
                    last_i = move_pos
            char_pos[c] = i

        max_len = max(max_len, len(s) - last_i)
        return max_len
