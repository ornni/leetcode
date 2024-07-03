# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        answer = 0

        while queue:
            now_sum = 0
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                now_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            answer = now_sum

        return answer