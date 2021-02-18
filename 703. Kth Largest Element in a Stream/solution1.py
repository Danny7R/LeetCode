class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.knums = nlargest(k, nums)
        heapify(self.knums)
        if(len(nums) < k): heappush(self.knums, -1e4)

    def add(self, val: int) -> int:
        heappushpop(self.knums, val)
        return self.knums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)