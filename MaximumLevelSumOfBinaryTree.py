# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return []
        queue = deque([root])
        
        res=float('-inf')
        l=1
        max_level=1
        while queue:
            sum=0
            n=len(queue)
            for i in range(n):
                node=queue.popleft()
                sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if sum>res:
                max_level=l
                res=sum
            l+=1
        return max_level

