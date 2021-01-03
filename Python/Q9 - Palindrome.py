# Determine whether an integer is a palindrome. 
# An integer is a palindrome when it reads the same 
# backward as forward.

# Results: Runtime: 40ms, Memory: 13.1MB
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # Temporary empty string
        returnStr = ""
        
        # Iterate through x and append elements in backwards order
        for i in str(x):
            returnStr = i + returnStr
        
        # Return true if palindrome
        return (returnStr == str(x))
