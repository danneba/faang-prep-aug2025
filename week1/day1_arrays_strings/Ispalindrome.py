class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr = list(str(x))
        n = len(arr)
        right = n-1
        for i in range(n):
            if arr[i] != arr[right]:
                return False
            right = right-1
        return True
    
if __name__ == '__main__':
    x = 121
    sol = Solution()
    print(sol.isPalindrome(x))
    


# optimized one

"""""
  class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr = list(str(x))
        n = len(arr)
        right = n-1
        for i in range(n):
            if arr[i] != arr[right]:
                return False
            right = right-1
        return True
""""""    