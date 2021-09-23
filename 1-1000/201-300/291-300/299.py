class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_count = {}
        guess_count = {}
        for i in "0123456789":
            secret_count[i] = 0
            guess_count[i] = 0

        A = 0
        B = 0
        for i in range(len(secret)):
            s = secret[i]
            g = guess[i]
            if s == g:
                A += 1
            else:
                secret_count[s] += 1
                guess_count[g] += 1

        for i in "0123456789":
            B += min(secret_count[i], guess_count[i])
        
        return f"{A}A{B}B"
