class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        max_final = max_i = nums[0]
        for num in nums[1:]:
            max_i = max(num, max_i + num)
            max_final = max(max_final, max_i)
        return max_final