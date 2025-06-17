class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))
if __name__ == "__main__":
    s = Solution()
    print(s.intersection([1, 2, 2, 1], [2, 1]))        
    print(s.intersection([4, 9, 5], [9, 5, 9, 8, 4])) 
    print(s.intersection([1, 3, 5], [2, 3, 4, 1]))        
    print(s.intersection([7, 8], [8, 9]))               
    print(s.intersection([4,6], [1, 2, 3]))                