class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ans = nums
        n = len(nums)
        for i in range(len(nums)):
            ans.append(nums[i])
        return ans