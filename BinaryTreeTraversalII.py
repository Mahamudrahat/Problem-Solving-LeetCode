# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue=collections.deque([root])
        output=[]
        
        while queue:
            helper=[]
            n=len(queue)
            for i in range(n):
                node=queue.popleft()
                helper.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(helper)
        output.reverse()
        return output
