class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        res=-1

        while l<=r:
            if nums[l]==target:
                res=l
                break
            elif nums[r]==target:
                res=r
                break
            else:
                mid=(l+r)//2
                if nums[mid]==target:
                    res=mid
                    break
                elif nums[l]<nums[mid]:
                    if nums[l]<=target<nums[mid]:
                        r=mid-1
                    else:
                        l=mid+1
                elif nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1


        return res

        