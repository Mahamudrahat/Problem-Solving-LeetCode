# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count=0
        def pathSumDetail(root):
            if not root:
                return 0
            hasSum(root,0)   
            pathSumDetail(root.left)
            pathSumDetail(root.right)
        def hasSum(root,curSum):
            
            if not root:
                return 0
            curSum+=root.val
            if curSum==targetSum:
                self.count+=1

            hasSum(root.left,curSum)
            hasSum(root.right,curSum)

        pathSumDetail(root)
        return self.count

        