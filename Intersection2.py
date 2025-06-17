class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        result = []
        for num in count1:
            if num in count2:
                min_count = min(count1[num], count2[num])
                result.extend([num] * min_count)
        return result
if __name__ == "__main__":
    s = Solution()
    print(s.intersect([1, 2, 2, 1], [2, 1]))        
    print(s.intersect([4, 9, 5], [9, 5, 9, 8, 4])) 
    print(s.intersect([1, 3, 5], [2, 3, 4, 1]))        
    print(s.intersect([7, 8], [8, 9]))               
    print(s.intersect([4,6], [1, 2, 3]))