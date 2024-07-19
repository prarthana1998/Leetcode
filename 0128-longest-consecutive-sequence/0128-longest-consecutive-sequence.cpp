class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int,int>mp;
        int ans = 0;
        int length = 0;
        for(int i=0; i<nums.size();i++)
        {
            mp[nums[i]]++;
        }
        for(int i=0; i<nums.size();i++)
        {
            if(mp.find(nums[i]-1)==mp.end())
            {
                length = 1;
                int num = nums[i]+1;
                while(mp.find(num)!=mp.end())
                {
                    length++;
                    num++;

                }
                 ans = max(ans, length);
            }
        }

       
        return ans;
        
    }
};