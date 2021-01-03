/*  Given an array of integers 'nums' and integer 'target', return (in
	any order) the indices of the two numbers such that they add up to the 
	target. Each input has one solution, so no duplicate returns. */

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
	
		// Create empty array
        vector<int> returnArr;
        
		// Iterate with 2D array, adding each index i and j
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < nums.size(); j++) {
			
				// If conditions met, add elements to return array
                if ((nums[i] + nums[j] == target) && (i != j)){
                    returnArr.push_back(i);
                    returnArr.push_back(j);
                }
            }    
        }
        
		// Remove last half of return array, as those are duplicates resulting from above loops
        returnArr.erase(returnArr.begin() + returnArr.size()/2, returnArr.end());
        
        return returnArr;
    }
};
