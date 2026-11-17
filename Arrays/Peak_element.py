class Solution:
    def peakElement(self,nums):
        n = len(nums)
        left = 0
        right = n-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

solution = Solution()
nums = list(map(int, input("Enter array elements: ").split()))
result = solution.peakElement(nums)
print("Index of a peak element:", result)
