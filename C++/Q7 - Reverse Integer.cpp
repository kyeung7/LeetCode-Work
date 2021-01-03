/* Given a 32-bit signed integer, reverse digits of an integer.
Assume we are dealing with an environment that could only store 
integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 
0 when the reversed integer overflows. */

// Results: Runtime: 0ms, Memory: 6.1MB
class Solution {
public:
    int reverse(int x) {
		
		// Create number y size of 32bits + 32 bits
        long long y = 0;
        
		// While x != 0
        while (x) {
			
			// Jump 10s place for y and add the digit in the 1s place from x
            y = y*10 + x%10;
			
			// Moves x's decimal place down so further mods get the 10s, 100s, ... digit
            x /= 10;
        }
		
		// If y ends up breaking constriant sizes (- or +) return 0 otherwise return y (now reversed)
        return (y < INT_MIN || y > INT_MAX) ? 0 : y;
    }
};