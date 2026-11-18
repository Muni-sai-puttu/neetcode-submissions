class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=len(nums)-1
        while i<j:
            mid=nums[i]+nums[j]
            if mid==target:
                return [i+1,j+1]
            elif mid>target:
                j-=1
            else:
                i+=1
        return []