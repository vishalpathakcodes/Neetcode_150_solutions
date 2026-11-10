class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        ans=0
        for num in numset:
            res=1
            if num-1 not in numset:
                while(num+1 in numset):
                    res+=1
                    num+=1
                ans=max(ans,res)
        return ans
