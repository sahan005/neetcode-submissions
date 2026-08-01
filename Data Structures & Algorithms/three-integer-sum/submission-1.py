class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        i=0

        for i in range(0, len(nums)):
            myset=set()
            for j in range(i+1, len(nums)):
                thrd=-(nums[i]+nums[j])
                if thrd in myset:
                    lst=sorted([nums[i], nums[j], thrd])
                    res.add(tuple(lst))
                myset.add(nums[j])
        
        return [list(x) for x in res]