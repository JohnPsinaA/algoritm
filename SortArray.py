class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and arr[left] > arr[largest]:
                largest = left
            
            if right < n and arr[right] > arr[largest]:
                largest = right
            
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            heapify(nums, n, i)
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, i, 0)
        return nums
if __name__ == "__main__":
    s = Solution()
    print(s.sortArray([5, 2, 3, 1]))
    print(s.sortArray([5, 2, 1, 2, 6, 0]))
    print(s.sortArray([1, 2, 3, 4, 5]))
    print(s.sortArray([5, 4, 3, 7, 1]))
    print(s.sortArray([9, 8, 5]))