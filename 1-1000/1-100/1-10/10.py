class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        edited_p = []
        for c in p:
            if c == "*":
                edited_p[-1][1] = "*"
            else:
                edited_p.append([c, 1])

        matchMap = []
        for i in range(len(s)):
            matchMap.append([None] * len(edited_p))

        def canMatch(i, j):
            if i == len(s) and j == len(edited_p):
                return True
            if j == len(edited_p):
                return False
            if i == len(s):
                if edited_p[j][1] == "*":
                    return canMatch(i, j+1)
                return False

            if matchMap[i][j] is True or matchMap[i][j] is False:
                return matchMap[i][j]

            if edited_p[j][0] == ".":
                if edited_p[j][1] == "*":
                    if canMatch(i, j+1):
                        matchMap[i][j] = True
                        return True
                    for _i in range(i, len(s)):
                        if canMatch(_i+1, j+1):
                            matchMap[i][j] = True
                            return True

                    matchMap[i][j] = False
                    return False

                else:
                    matchMap[i][j] = canMatch(i+1, j+1)
                    return matchMap[i][j]
            if s[i] == edited_p[j][0]:
                if edited_p[j][1] == "*":
                    if canMatch(i, j+1):
                        matchMap[i][j] = True
                        return True

                    for _i in range(i, len(s)):
                        if s[_i] != edited_p[j][0]:
                            break
                        if canMatch(_i+1, j+1):
                            matchMap[i][j] = True
                            return True

                    matchMap[i][j] = False
                    return False
                else:
                    matchMap[i][j] = canMatch(i+1, j+1)
                    return matchMap[i][j]
            else:
                if edited_p[j][1] == "*":
                    matchMap[i][j] = canMatch(i, j+1)
                    return matchMap[i][j]
                else:
                    matchMap[i][j] = False
                    return False

        return canMatch(0, 0)
