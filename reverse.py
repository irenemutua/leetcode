class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse digits of a 32-bit signed integer.
        Returns 0 if the reversed integer overflows.
        """
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_num = int(str(x_abs)[::-1]) * sign

        if -(2*31) <= reversed_num <= (2*31 - 1):
            return reversed_num
        return 0


# Example test
if _name_ == "_main_":
    print(Solution().reverse(123))   # 321
    print(Solution().reverse(-123))  # -321
    print(Solution().reverse(120))   # 21