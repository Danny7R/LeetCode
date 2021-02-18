class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            i = nums.index(num)
            if (target - num) in nums:
                if target - num == num and nums.count(num) > 1:
                    dic = dict(zip(nums, range(len(nums))))
                    return [i, dic.get(nums[i])]
                elif target - num != num: return [i, nums.index(target - num)]