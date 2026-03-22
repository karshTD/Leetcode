class Solution {
public:
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int start = 0;
        for(int i = 0; i < nums.size(); i ++){
            if(nums[i] != start){
                return start;
            }
            start++;
        }

        return start;
    }
};