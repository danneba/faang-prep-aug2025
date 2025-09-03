class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        seen = set()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, n-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right = right-1
                elif total < 0:
                    left = left+1
                else:
                    seen.add(tuple(sorted([nums[i],nums[left], nums[right]])))
                    left += 1
                    right -= 1
        return [list(t) for t in seen]         
if __name__ == 'main':
    nums = [-1,0,1,2,-1,-4]
    ans = Solution()
    print(ans.threeSum(nums))