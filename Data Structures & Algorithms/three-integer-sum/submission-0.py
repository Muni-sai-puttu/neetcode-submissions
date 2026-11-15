class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s=set()
        n=len(nums)
        for i in range(n-2):
            j=i+1
            k=n-1
            while j<k:
                total=nums[i]+nums[j]+nums[k]
                if total==0:
                    s.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif total>0:
                    k-=1
                else:
                    j+=1
        return [list(x) for x in s]