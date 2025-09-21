class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Check if an integer is a palindrome without converting
        the whole number to a string.
        """
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10


# Example test
if _name_ == "_main_":
    print(Solution().isPalindrome(121))   # True
    print(Solution().isPalindrome(-121))  # False
    print(Solution().isPalindrome(10))    # False