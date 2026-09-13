class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count= Counter(tasks)
        h=[-cnt for cnt in count.values()]
        heapq.heapify(h)

        time=0
        q=deque()

        while q or h:
            time+=1

            if len(h)!=0:
                cnt= 1+heapq.heappop(h)
                if cnt!=0:
                    q.append([cnt, time+n])
                
            if len(q)!=0 and q[0][1]==time:
                heapq.heappush(h, q.popleft()[0])

        return time