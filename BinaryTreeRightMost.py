# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []  # If the root is None, return an empty list.

        queue = deque([root])
        res = []

        while queue:
            n = len(queue)  # Number of nodes at the current level.

            for i in range(n):
                node = queue.popleft()

                
                    

                # Append left and right children of the current node.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(node.val)

        return res