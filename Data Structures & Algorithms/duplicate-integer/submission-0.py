class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasAppeared={}
        for num in nums:
            if num in hasAppeared:
                return True;
            else:
                hasAppeared[num]=1
        return False
        