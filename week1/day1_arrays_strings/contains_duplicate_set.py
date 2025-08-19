from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        for i in range(len(nums)):
            if nums[i] not in duplicate:
                duplicate.add(nums[i])
            else:
                return True
        return False


if __name__ == "__main__":
    nums = [1,2,3,1]
    print(Solution().containsDuplicate(nums))