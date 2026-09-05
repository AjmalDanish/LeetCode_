class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
        max_num = nums[0]
        for i in range(n):
            max_num = max(max_num, nums[i])
            diff = max_num - suffix_min[i]
            if diff <= k:
                return i
        return -1