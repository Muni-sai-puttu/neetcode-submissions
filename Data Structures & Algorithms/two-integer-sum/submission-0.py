class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            ans=target-nums[i]
            if ans in h.keys():
                return [h[ans],i]
            else:
                h[nums[i]]=i
                