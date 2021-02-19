class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNums = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in seenNums:
                seenNums[num] = i
            else:
                return [seenNums[n], i]