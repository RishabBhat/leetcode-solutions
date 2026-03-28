"""
Problem: All Nodes Distance K in Binary Tree
Link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
Difficulty: medium

Approach:
dfs through the tree and build a parent map to keep track of parent pointers
then do bfs and create a queue of every level of nodes. 
use a visited set so we don't revisit nodes, since we're starting the bfs from 
the target
when the level is == k, we know that every node in the queue is 
k distance, so we can just return the values in the queue

Time Complexity: O(N)
Space Complexity: O(N)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}

        def dfs(node, par):
            if not node:
                return
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)

        q = deque([target])
        visited = {target}
        level = 0

        while q:
            if level == k:
                return [node.val for node in q]
            
            for _ in range(len(q)):
                node = q.popleft()

                for nei in [node.left, node.right, parent[node]]:
                    if nei and nei not in visited:
                        visited.add(nei)
                        q.append(nei)
                
            level += 1
        return []

