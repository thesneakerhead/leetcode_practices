def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevHash = {}
        for i, n in enumerate(nums):
            diff = target -n
        # Check if number has already been iterated over and return index that is stored in dictionary (if it has)
            if diff in prevHash:
                return [prevHash[diff], i]
         # Else store current number value, index in the history of iterated numbers
            prevHash[n] = i
        return
        
