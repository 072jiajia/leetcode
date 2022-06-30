class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_string = str(x)
        return num_string == num_string[::-1]
