class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            middle = l + (r - l) // 2

            if middle + 1 < len(nums) and nums[middle] > nums[middle + 1]: return nums[middle + 1]
            if middle - 1 >= 0 and nums[middle - 1] > nums[middle]: return nums[middle]

            if nums[middle] == nums[l] and nums[l] == nums[r]:
                if l + 1 < len(nums) and nums[l] > nums[l + 1]: return nums[l + 1]
                l += 1
                if r - 1 >= 0 and nums[r - 1] > nums[r]: return nums[r]
                r -= 1
            elif nums[l] <= nums[middle] and nums[middle] > nums[r]: l = middle + 1
            else: r = middle
        
        return nums[l]
