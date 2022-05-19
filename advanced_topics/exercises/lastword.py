#  https://leetcode.com/problems/length-of-last-word/

class Solution(object):
    def lengthOfLastWord(self, s):
        self.z = s.split()
        self.l = self.z[-1]
        print(f'The last word is {self.l} with length of {len(self.l)}')


sol = Solution()
sol.lengthOfLastWord("water now rower vitam")
