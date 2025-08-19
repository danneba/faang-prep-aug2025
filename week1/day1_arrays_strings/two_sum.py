from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_pair = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in sum_pair:
                return [sum_pair[diff], i]
            else:
                sum_pair[nums[i]] = i

if __name__ == "__main__":
    # Local test cases
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target)) 
