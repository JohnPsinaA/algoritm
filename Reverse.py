class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
if __name__ == "__main__":
    s = Solution()
    test_cases = [
        ["h", "e", "l", "l", "o"],
        ["S", "u", "m", "s", "u", "n", "g"],
        ["a", "b", "o", "b", "akro"],
        ["r", "e", "v", "e", "r", "s", "e"],
        ["t", "i", "k", "st"]
    ]
    
    for case in test_cases:
        s.reverseString(case)
        print(case)