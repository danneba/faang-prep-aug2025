from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        Maxcount = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count = count + 1
                if count > Maxcount:
                    Maxcount = count
            else:
                count = 0

        return Maxcount

if __name__ == '__main__':
    nums = [1,1,0,1,1,1]
    sol = Solution()
    print(sol.findMaxConsecutiveOnes(nums))