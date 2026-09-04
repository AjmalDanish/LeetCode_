class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for j in range(len(nums)):
            max_num = max(nums[:j+1])
            min_num = min(nums[j:])
            diff = max_num - min_num
            if diff <= k:
                return j
        return -1