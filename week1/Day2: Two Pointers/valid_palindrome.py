from typing import List
class Solution:
    def isPalindrome(self, s: str) -> bool:
        removed = ''.join(ch for ch in s if ch.isalnum())
        arr = list(removed.lower())
        n = len(arr)

        left, right = 0, n-1
        while left < right:
            if arr[left] != arr[right]:
                return False
            left = left+1
            right = right-1
        return True

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    ans =  Solution()
    print(ans.isPalindrome(s))