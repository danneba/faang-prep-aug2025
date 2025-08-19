from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupl = {}
        for i in range(len(nums)):
            dupl[nums[i]] = dupl.get(nums[i],0) + 1
            if dupl[nums[i]] > 1:
                return True

        return False


if __name__ == "__main__":
    nums = [1,2,3,1]
    print(Solution().containsDuplicate(nums))