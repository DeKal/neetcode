# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        q = deque([(root.val, root)])
        res = 1
        while q:
            print(q)
            val, top = q.popleft()

            if top.left:
                if val <= top.left.val:
                    res+=1
                q.append((max(val, top.left.val), top.left))
            if top.right:
                if val <= top.right.val:
                    res+=1
                q.append((max(val, top.right.val), top.right))
            


        return res

