class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        count = {}
        for num in arr1:
            count[num] = count.get(num, 0) + 1
        
        result = []
        for num in arr2:
            if num in count:
                result.extend([num] * count[num])
                del count[num]
        
        for num in sorted(count.keys()):
            result.extend([num] * count[num])
        
        return result
if __name__ == "__main__":
    s = Solution()
    print(s.relativeSortArray([2, 3, 1, 4, 5], [3, 2, 1]))
    print(s.relativeSortArray([5, 6, 7, 8], [8, 7, 6]))
    print(s.relativeSortArray([1, 2, 3], [3, 2]))
    print(s.relativeSortArray([10, 20, 30], [20, 10]))
    print(s.relativeSortArray([4, 5, 6], [5, 4]))