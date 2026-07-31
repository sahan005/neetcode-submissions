class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset=set()
        for i in range(0,len(nums)):
            if nums[i] not in myset:
                myset.add(nums[i])
            elif nums[i] in myset:
                return True
        return False