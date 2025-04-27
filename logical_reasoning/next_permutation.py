class Solution:
    def nextPermutation(self, nums):
        # Step 1: Find the first decreasing element from the end
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: Find the element just larger than nums[i] to swap with
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1

            # Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the portion after index i
        nums[i + 1:] = reversed(nums[i + 1:])


nums = [3, 2, 1]
s = Solution()
s.nextPermutation(nums)
print(nums)
