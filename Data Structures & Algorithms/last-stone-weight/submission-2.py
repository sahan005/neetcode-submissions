class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h=[]
        heapq.heapify(h)

        for n in stones:
            heapq.heappush(h, -n)
        
        while len(h)>1:
            n1=abs(heapq.heappop(h))
            n2=abs(heapq.heappop(h))
            if n1==n2:
                continue
            elif n1>n2:
                heapq.heappush(h, -(n1-n2))
            elif n2>n1:
                heapq.heappush(h, -(n2-n1))
            
            
        if len(h)==0:
            return 0
        else:
            last=abs(heapq.heappop(h))
            return last


        



        