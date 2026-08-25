class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        n = len(nums)
        result = []
        for i in range(0, n):
            if i%10== nums[i]:
                return i
        return -1