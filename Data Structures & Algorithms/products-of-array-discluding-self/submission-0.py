class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        p=0
        
        for i in range(0,len(nums)):
            lp=1
            rp=1
            for k in range(0, p):
                lp=lp*nums[k]
            for j in range(p+1, len(nums)):
                rp=rp*nums[j]
            tp=lp*rp
            res[i]=tp
            p+=1

        return res



            


        


        
        