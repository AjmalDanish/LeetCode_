class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n -1 
        while left < right:
            sums = numbers[left] + numbers[right]
            if sums > target :
                right -= 1
            elif sums < target :
                left += 1
            else:
                return [left+1,right+1]