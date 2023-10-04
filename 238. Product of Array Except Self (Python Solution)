class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        leftprod, rightprod = 1,1
        n = len(nums)
        answer = [1]*n

        for i in range(n):
            answer[i] *= leftprod
            leftprod *= nums[i]

        for i in range(n-1, -1,-1):
            answer[i] *= rightprod
            rightprod *= nums[i]
        return answer
