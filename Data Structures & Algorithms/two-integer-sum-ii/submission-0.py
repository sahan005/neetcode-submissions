class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp=0
        rp=len(numbers)-1
        
        while lp<rp:
            check=numbers[lp]+numbers[rp]
            if check>target:
                rp=rp-1
            elif check<target:
                lp=lp+1
            elif check==target:
                return [lp+1,rp+1]
            

        