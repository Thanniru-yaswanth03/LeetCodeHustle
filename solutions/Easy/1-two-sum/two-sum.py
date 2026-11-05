# Problem: 1. Two Sum
# Difficulty: Easy
# Language: Python 3
# Performance: 50 ms (beats 75%), 16.0 MB (beats 70%)
# LeetCode: https://leetcode.com/problems/two-sum/
# Synchronized via StreakForge at 2026-11-05T10:38:52.021Z

1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        pair_idx = {}
4
5        for i, num in enumerate(nums):
6            if target - num in pair_idx:
7                return [i, pair_idx[target - num]]
8            pair_idx[num] = i