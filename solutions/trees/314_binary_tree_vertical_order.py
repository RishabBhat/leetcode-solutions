"""
Problem: [Title]
Link: https://leetcode.com/problems/[slug]/
Difficulty: [Easy/Medium/Hard]

Approach:
the trick to this problem is to keep track of the columns
and do a bfs. we just subtract a column
if we're adding left child and add a column if we're adding
a right child. we also have a trick to optimize with
keeping track of the min and max values so we don't
need to sort the array to traverse in the right order

Time Complexity: O()
Space Complexity: O()
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        columns = defaultdict(list)
        q = deque([(root, 0)])
        min_col = 0
        max_col = 0

        while q:
            print(q)
            node, col = q.popleft()
            columns[col].append(node.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))

        
        res = []

        for i in range(min_col, max_col + 1):
            res.append(columns[i])
        return res

