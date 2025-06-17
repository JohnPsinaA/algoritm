class Solution(object):
    def heightChecker(self, heights):
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count
        
if __name__ == "__main__":
    s = Solution()
    print(s.heightChecker([1, 1, 6, 2, 1, 7, 5]))
    print(s.heightChecker([1, 3, 3, 5, 1]))  
    print(s.heightChecker([5, 1, 2, 3, 4]))        