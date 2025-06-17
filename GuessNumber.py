
picked_number = 6  

def guess(num):
    if num > picked_number:
        return -1
    elif num < picked_number:
        return 1
    else:
        return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            if result == 0:
                return mid  
            elif result < 0:
                right = mid - 1
            else:
                left = mid + 1  
if __name__ == "__main__":
    s = Solution()
    print(s.guessNumber(10))
    print(s.guessNumber(1))
    print(s.guessNumber(2))