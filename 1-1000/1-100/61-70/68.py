from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        waiting = []
        waiting_len = -1
        all_space_len = maxWidth
        for word in words:
            added_len = waiting_len + 1 + len(word)
            if added_len > maxWidth:
                if len(waiting) == 1:
                    output.append(waiting[0] + ' ' * all_space_len)
                else:
                    num_space = len(waiting) - 1
                    space_len = all_space_len // num_space
                    remain_space = all_space_len % num_space
                    big_space = ' ' * (space_len + 1)
                    small_space = ' ' * space_len
                    line = ''
                    for i in range(remain_space):
                        line += waiting[i] + big_space
                    for i in range(remain_space, num_space):
                        line += waiting[i] + small_space
                    line += waiting[-1]
                    output.append(line)

                waiting_len = len(word)
                waiting = [word]
                all_space_len = maxWidth - waiting_len
            else:
                all_space_len -= len(word)
                waiting.append(word)
                waiting_len = added_len

        if len(waiting) == 1:
            output.append(waiting[0] + ' ' * (maxWidth - len(waiting[0])))
        else:
            line = ''
            for wword in waiting[:-1]:
                maxWidth -= (len(wword) + 1)
                line += wword + ' '
            line += waiting[-1] + ' ' * (maxWidth - len(waiting[-1]))
            output.append(line)
        return output
