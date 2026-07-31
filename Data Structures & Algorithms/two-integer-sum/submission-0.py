class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i in range(0,len(nums)):
            rem=target-nums[i]
            if nums[i] in hm:
                p=hm[nums[i]]
                q=i
                return [p,q]
            else:
                hm[rem]=i
        
            
        

        
        
    
            

