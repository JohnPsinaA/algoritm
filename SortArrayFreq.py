class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        sorted_nums = sorted(nums, key=lambda x: (count[x], -x))
        
        return sorted_nums
if __name__ == "__main__":
    s = Solution()
    print(s.frequencySort([1, -1, -2, 2, -2, 3]))  
    print(s.frequencySort([4, -5, 6, 4, -5]))      
    print(s.frequencySort([-10, -20, 10]))          
    print(s.frequencySort([7, 8, 7, 9]))                         