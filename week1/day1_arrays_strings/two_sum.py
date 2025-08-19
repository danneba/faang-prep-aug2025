from typing import List 

class Solution:
    def twoSum(self, nums:List[int], target: int)-> List[int]:
        length = len(nums)
        for i in range(length):
            for j in range(length):
                if i != j and nums[i] + nums[j] == target:
                    return [i , j]
                else:
                    continue

if __name__ == "__main__":
    # Local test cases
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target)) 
