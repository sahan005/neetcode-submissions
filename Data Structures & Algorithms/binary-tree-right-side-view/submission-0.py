# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=deque()
        op=[]
        if root==None:
            return []
        q.append(root)

        while q:
            level=[]
            for _ in range(len(q)):
                e=q.popleft()
                if e!=None:
                    level.append(e.val)
                    q.append(e.left)
                    q.append(e.right)
            
            if level:
                op.append(level[-1])
        
        return op
        
                

