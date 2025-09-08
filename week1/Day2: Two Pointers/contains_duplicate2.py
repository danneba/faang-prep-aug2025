from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i in range(len(nums)):
            j = nums[i]
            if j in seen and i - seen[j] <= k:
                return True
            seen[j] = i
        return False 

if __name__ == "__main__":
    nums= [1,2,3,1]
    k = 3
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, k))