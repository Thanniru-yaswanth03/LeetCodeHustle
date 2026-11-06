# Problem: 2620. Counter
# Difficulty: Easy
# Language: Python 3
# Performance: 50 ms (beats 75%), 16.0 MB (beats 70%)
# LeetCode: https://leetcode.com/problems/counter/
# Synchronized via StreakForge at 2026-11-06T04:56:32.870Z

function createCounter(start) {
  let count = start;
  return function() {
    return count++;
  }
}