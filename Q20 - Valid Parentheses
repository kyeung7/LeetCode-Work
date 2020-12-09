# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
# Determine if the input string is valid.

# Runtime:44 ms, Memory: 13.6 MB
class Solution(object):
    def isValid(self, s):
    
        # Iterate through s, 'delete' paren-pairs
        for char in s:
            s = s.replace("()", "").replace("[]", "").replace("{}", "")
        
        # Return of s is empty (even # of parens, valid pairs)
        return (s == "")
       
        """
        :type s: str
        :rtype: bool
        """
