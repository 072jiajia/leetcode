class Solution:
    def dfs(self, index, state, table, courses):
        if index in table:
            state[index] = 1
            for prev in table[index]:
                if state[prev] == 2:
                    continue
                if state[prev] == 1:
                    return False
                if not self.dfs(prev, state, table, courses):
                    return False
        courses.append(index)
        state[index] = 2
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        state = [0] * numCourses
        table = {}
        for x, y in prerequisites:
            if x in table:
                table[x].append(y)
            else:
                table[x] = [y]

        courses = []
        for i in range(numCourses):
            if state[i] != 2:
                if not self.dfs(i, state, table, courses):
                    return []
        return courses
