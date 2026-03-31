# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        results = []

        cur_lv = [root]
        nxt_lv = []
        while cur_lv:
            res = []
            for node in cur_lv:
                if node.left:
                    nxt_lv.append(node.left)
                if node.right:
                    nxt_lv.append(node.right)
                res.append(node.val)

            results.append(res)
            cur_lv = nxt_lv
            nxt_lv = []

        return results

