from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        key = ""
        for i in range(len(letters)):
            if letters[i] > target:
                key = letters[i]
            elif i == len(letters) -1 and letters[i] <= target:
                return letters[0]
            else:
                continue
            for j in range(i, len(letters)):
                if key > letters[j]:
                    break
            return key
        
        
if __name__ == "__main__":
    letters = ["c","f","j"]
    target = "j"
    sol = Solution()
    print(sol.nextGreatestLetter(letters, target))