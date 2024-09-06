class Solution:
    def __init__(self):
        self.maxPath = 0
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.solve(root,0,True)
        self.solve(root,0,False)
        return self.maxPath
    def solve(self,root,step,goleft):
        if root is None:
            return
        self.maxPath=max(self.maxPath,step)
        if goleft==True:
            self.solve(root.left,step+1,False)
            self.solve(root.right,1,True)
        else:
            self.solve(root.right,step+1,True)
            self.solve(root.left,1,False)
