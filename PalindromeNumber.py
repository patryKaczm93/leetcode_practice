class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Given an integer x, return True if x is a palindrome, and False otherwise.
        
        A palindrome is a number that reads the same forward and backward.
        Example:
        - 121 -> True
        - -121 -> False (because '-' makes it asymmetric)
        - 10 -> False
        """
        x_as_list = [char for char in str(x)]

        for i, j in zip(x_as_list, reversed(x_as_list)):
            if i != j:
                return False
        
        return True 

a = Solution()
print(a.isPalindrome(-123))  # Expected output: False
print(a.isPalindrome(121))   # Expected output: True
print(a.isPalindrome(10))    # Expected output: False