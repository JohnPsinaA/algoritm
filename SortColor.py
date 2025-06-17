class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums
if __name__ == "__main__":
    s = Solution()
    print(s.sortColors([2, 0, -2, 1, 1, 10]))
    print(s.sortColors([2, 4, 1]))
    print(s.sortColors([0, 1.5, 2]))
    print(s.sortColors([1, 2, 0]))
    print(s.sortColors([0, 0, 1, 1, 2, 2]))