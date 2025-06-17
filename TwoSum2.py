class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 13
            else:
                right -= 1
        return []
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))      
    print(s.twoSum([2, 3, 4], 6))  
    print(s.twoSum([3, 3], 6))              
    print(s.twoSum([-1,0], -1))        
    print(s.twoSum([0, -1, 2, -3], -3))