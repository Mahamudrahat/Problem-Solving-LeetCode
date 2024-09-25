# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        currTree=root
        if currTree is None:
                return None
        while(currTree):
            if currTree.val==val:
              return currTree
            elif val<currTree.val:
               currTree=currTree.left
            else:
                currTree=currTree.right
        return currTree