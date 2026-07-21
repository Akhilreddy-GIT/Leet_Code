class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Negative numbers are never palindromes.
        # Numbers ending in 0 (except 0 itself) can't be palindromes.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0

        while x > rev:
            digit = x % 10          # Take last digit
            rev = rev * 10 + digit  # Build reversed half
            x //= 10                # Remove last digit

        # Even digits: x == rev
        # Odd digits: x == rev // 10 (ignore the middle digit)
        return x == rev or x == rev // 10