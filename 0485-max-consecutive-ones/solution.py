class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=cnt=0
        for num in nums:
            if num==1:
                cnt+=1
            else:
                res=max(res,cnt)
                cnt=0
        return max(res,cnt)
