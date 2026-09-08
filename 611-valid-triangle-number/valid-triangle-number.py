class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for right in range(n - 1, 1, -1):
            left = 0
            mid = right - 1
            while left < mid:
                if nums[left] + nums[mid] > nums[right]:
                    count += mid - left
                    mid -= 1
                else:
                    left += 1
        return count