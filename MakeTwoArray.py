class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        count = {}
        for num in target:
            count[num] = count.get(num, 0) + 1
        
        for num in arr:
            if num in count:
                count[num] -= 1
                if count[num] == 0:
                    del count[num]
            else:
                return False
        
        return len(count) == 0 
if __name__ == "__main__":
    s = Solution()
    print(s.canBeEqual([1, 2, 3, 4], [2, 1, 4, 3]))  
    print(s.canBeEqual([1, 2, 3], [3, 2, 1]))        
    print(s.canBeEqual([1, 2, 2], [2, 1, 1]))        
    print(s.canBeEqual([5, 6, 7], [7, 5, 8]))        
    print(s.canBeEqual([10, 20], [20, 10]))          