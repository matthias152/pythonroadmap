class Solution(object):
    def majorityElement(self, nums):
        self.dicti = {}
        for i in nums:
            if str(nums[i]) in self.dicti.keys():
                self.dicti[str(i)] = 1
            else:
                self.dicti[str(i)] += 1
        print(self.dicti)
        # print(max(zip(self.dicti.values(), self.dicti.keys()))[1])


stanc = Solution()
stanc.majorityElement([2, 2, 2 , 2, 1, 1])
