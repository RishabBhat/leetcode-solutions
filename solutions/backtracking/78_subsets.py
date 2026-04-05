"""
Problem: Subsets
Link: https://leetcode.com/problems/subsets/
Difficulty: Medium

Approach:
Backtracking. At each index, branch into two choices: include the current
element or skip it. Recurse through all indices, adding the current subset
to the result at every call.

Time Complexity: O(n * 2^n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res