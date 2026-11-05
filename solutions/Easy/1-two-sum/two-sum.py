# Problem: 1. Two Sum
# Difficulty: Easy
# Language: Python 3
# Performance: 52 ms (beats 88.5%), 17.0 MB (beats 79.2%)
# LeetCode: https://leetcode.com/problems/two-sum/
# Synchronized via StreakForge at 2026-11-05T10:40:00.000Z

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev:
                return [prev[diff], i]
            prev[n] = i
        return []
