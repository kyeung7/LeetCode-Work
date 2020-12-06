# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Results: Runtime: 16ms, Memory: 13.7MB
class Solution(object):
    def longestCommonPrefix(self, strs):
		
		# Special case - empty list
        if len(strs) == 0:
            return ""

        # Get shortest string in strs by sorting (by length) and getting smallest element
        shortStr = min(strs, key = len)

		# Iterate through the smallest string, checking for matches to strings in strs
        for i, char in enumerate(shortStr):
            for string in strs:
				
				# If a character in a string in strs does not match the letter then splice and return
                if string[i] != char:
                    return shortStr[:i]
					
        return shortStr 
		
		"""
        :type strs: List[str]
        :rtype: str
        """