class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        sub = list(s)
        count = 0
        length = 0
        n = len(sub)

        for i in range(n):
            seen.clear()
            for j in range(i, n):
                if sub[j] not in seen:
                    seen.add(sub[j])
                    if j > i and sub[j-1] not in seen:
                        seen.add(sub[j-1])
                    length = len(seen)
                else:
                    break
                   
                if length > count:
                    count = length
        return count

if __name__ == "main":
    s = "abcabcbb"
    ans = Solution()
    print(ans.lengthOfLongestSubstring(s))