class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum=0
        maxsum=nums[0]

        for i in range(0,len(nums)):
            currsum=currsum+nums[i]
            maxsum=max(currsum, maxsum)
        
            if currsum<0:
                currsum=0
        
        return maxsum