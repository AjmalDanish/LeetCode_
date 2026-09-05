class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # freq = {}
        # for x in nums :
        #     freq[x] = freq.get(x,0) + 1
        # for key,value in freq.items():
        #     if value > 1:
        #         return True
        # return False
        seen = set()

        for x in nums:
            if x in seen:
                return True

            seen.add(x)

        return False
        