#  https://leetcode.com/problems/remove-duplicates-from-sorted-list/
class Solution(object):
    def deleteDuplicates(self, head):
        newArr = []
        for i in head:
            if i not in newArr:
                newArr.append(i)
        print(newArr)

stanc = Solution()
stanc.deleteDuplicates([1,1,1,2,2,2,3,3])
