class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target - nums[i]) in nums:
                if target - nums[i] == nums[i] and nums.count(nums[i]) > 1:
                    nums.reverse()
                    return [i, ((len(nums) - 1) - nums.index(target - nums[i]))]
                elif target - nums[i] != nums[i]: return [i, nums.index(target - nums[i])]