class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk=[]
        p=[]
        for i in range(0, len(speed)):
            p.append((position[i], speed[i]))

        p.sort(reverse=True)
        stk.append(p[0])
        pos, sp=p[0]
        time=(target-pos)/sp

        for posi, spe in p:
            timec=(target-posi)/spe
            if timec>time:
                stk.append(p[i])
                time=timec
            
        return len(stk)
            


            




        
        
        
        