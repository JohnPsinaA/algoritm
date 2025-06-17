class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index
        return []
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))      
    print(s.twoSum([7,5, 3], 8))             
    print(s.twoSum([3, 3], 6))                
    print(s.twoSum([1, 5, 3, 4], 8))          
    print(s.twoSum([0, -1, 2, -3], -3))       