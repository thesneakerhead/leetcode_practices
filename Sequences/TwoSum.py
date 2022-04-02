def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevHash = {}
        for i, n in enumerate(nums):
            diff = target -n
            if diff in prevHash:
                return [prevHash[diff], i]
            prevHash[n] = i
        return
        