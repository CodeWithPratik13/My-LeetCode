class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = nums + nums
        return result
a = Solution()
a.getConcatenation(nums= [1,2,1])