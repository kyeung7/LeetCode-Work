/* Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

1. I can be placed before V (5) and X (10) to make 4 and 9. 
2. X can be placed before L (50) and C (100) to make 40 and 90. 
3. C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. */

# Runtime: 36ms Memory: 13.2MB

# Set of special cases for roman numerals
special = {"IV", "IX", "XL", "XC", "CD", "CM"}

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Temporary indexing variables
        sum = 0
        i = 0
        
        # Iterate for length of s, check every letter and preceeding letter for special cases
        while i in range(len(s)):
        
            # If pair is special, convert a spliced string of that pair and update indexer
            if (s[i:i+2]) in special:
                sum += self.convert(s[i:i+2])
                i += 2
            # Otherwise convert single roman numeral and only update index by 1
            else:
                sum += self.convert(s[i])
                i += 1
                
        return sum
    
    # Conversion method, letter -> value, simply to keep main function clean
    def convert(self, roman):
        if roman == "I":
            return 1
        elif roman == "V":
            return 5
        elif roman == "X":
            return 10
        elif roman == "L":
            return 50
        elif roman == "C":
            return 100
        elif roman == "D":
            return 500
        elif roman == "M":
            return 1000
        
        # Special cases below
        elif roman == "IV":
            return 4
        elif roman == "IX":
            return 9
        elif roman == "XL":
            return 40
        elif roman == "XC":
            return 90
        elif roman == "CD":
            return 400
        elif roman == "CM":
            return 900
        
