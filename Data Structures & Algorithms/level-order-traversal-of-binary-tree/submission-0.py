# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        q=deque()

        q.append(root)
        while len(q)!=0:
            qlen=len(q)
            lvl=[]
            for i in range(qlen):
                e=q.popleft()
                if e is not None:
                    lvl.append(e.val)
                    q.append(e.left)
                    q.append(e.right)
            if len(lvl)>0:
                res.append(lvl)
        
        return res
            


        


        