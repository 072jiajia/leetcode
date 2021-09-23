from queue import PriorityQueue

def count_transformation(A, B):
    diff_count = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            diff_count += 1
    return diff_count

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int: 
        word_set = set(wordList)
        if beginWord == endWord:
            return 0
        if endWord not in word_set:
            return 0

        Q = PriorityQueue()
        Q.put((1, (1, beginWord, -1)))
        n = len(beginWord)
        while not Q.empty():
            _, (step, word, last_changed) = Q.get()
            for i in range(n):
                if i == last_changed:
                    continue
                left = word[:i]
                right = word[i + 1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    new = left + j + right
                    if new == endWord:
                        return step + 1
                    if new in word_set:
                        word_set.remove(new)
                        Q.put((step + 1 + count_transformation(new, endWord), (step + 1, new, i)))
        return 0
