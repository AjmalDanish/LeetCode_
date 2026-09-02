class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        n = len(nums)
        left_min = [float('inf')] * n
        right_min = [float('inf')] * n
        minimum = float('inf')
        for i in range(n):
            left_min[i] = minimum
            minimum = min(minimum, nums[i])
        minimum = float('inf')
        for i in range(n - 1, -1, -1):
            right_min[i] = minimum
            minimum = min(minimum, nums[i])
        ans = float('inf')
        for j in range(n):
            if left_min[j] < nums[j] and right_min[j] < nums[j]:
                ans = min(
                    ans,
                    left_min[j] + nums[j] + right_min[j]
                )
        return -1 if ans == float('inf') else ans