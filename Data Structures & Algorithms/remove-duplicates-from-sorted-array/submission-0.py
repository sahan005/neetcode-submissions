class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        k=1

        while k<len(nums):
            if nums[k]==nums[k-1]:
                k+=1
            elif nums[k] != nums[k-1]:
                nums[l]=nums[k]
                k+=1
                l+=1
            
        return l
            
        

    
        