import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        heap=[]

        for i in range(0,len(nums)):
            if nums[i] not in hm:
                hm[nums[i]]=1
            else:
                hm[nums[i]]+=1
        

        for num, count in hm.items():
            heapq.heappush(heap, (count, num))

            if len(heap)>k:
                heapq.heappop(heap)
        
        res=[]

        for count, num in heap:
            res.append(num)
        
        return res
