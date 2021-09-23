class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        splits = {}
        for c in 'abcdefghijklmnopqrstuvwxyz':
            splits[c] = []
        for word in words:
            splits[word[0]].append(word[1:])
        
        count = 0
        for c in s:
            remains = splits[c]
            splits[c] = []
            for remain in remains:
                if len(remain):
                    splits[remain[0]].append(remain[1:])
                else:
                    count += 1
        return count
