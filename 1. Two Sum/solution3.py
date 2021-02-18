class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target - nums[i]) in nums:
                if target - nums[i] == nums[i] and nums.count(nums[i]) > 1:
                    dic = dict(zip(nums, range(len(nums))))
                    return [i, dic.get(nums[i])]
                elif target - nums[i] != nums[i]: return [i, nums.index(target - nums[i])]