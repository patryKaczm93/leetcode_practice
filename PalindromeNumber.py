class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_as_list = [x for x in str(x)]


        for i,j in zip(x_as_list, reversed(x_as_list)):
            if i == j:
                return True
            else:
                return False
            




a = Solution()
a.isPalindrome(-123)