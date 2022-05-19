#  https://leetcode.com/problems/richest-customer-wealth
class Solution(object):
    def maximumWealth(self, accounts):
        highest = 0
        for i in accounts:
            if sum(i) > highest:
                highest = sum(i)
        return highest
