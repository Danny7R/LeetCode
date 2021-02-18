class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapify(nums)
        while(len(nums) > k): heappop(nums)
        if(len(nums) < k): heappush(nums, -1e4)
        self.knums = nums

    def add(self, val: int) -> int:
        heappushpop(self.knums, val)
        return self.knums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)