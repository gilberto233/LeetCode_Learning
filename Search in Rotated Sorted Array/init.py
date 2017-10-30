class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not len( nums ) or ( not target in nums ):
            return -1
        self.nums = nums
        self.target = target
        return self._dichotomy( 0, len( nums ) )

    def _dichotomy(self, start, end):
        middleIndex = start + int( ( end - start ) / 2 )
        if self.target == self.nums[ middleIndex ]:
            return middleIndex
        else:
            if self.nums[0] > self.nums[ middleIndex ]:
                if self.target > self.nums[ middleIndex ] and self.target <= self.nums[ end - 1 ]:
                    # normal dichotomy
                    return self._normalDichotomy( middleIndex + 1, end )
                else:
                    # self._dichotomy
                    return self._dichotomy( start, middleIndex )
            else:
                if self.target < self.nums[ middleIndex ] and self.target >= self.nums[0]:
                    # normal dichotomy
                    return self._normalDichotomy( start, middleIndex )
                else:
                    # self._dichotomy
                    return self._dichotomy( middleIndex + 1, end )

    def _normalDichotomy(self, start, end):
        middleIndex = start + int( ( end - start ) / 2 )
        if self.target == self.nums[ middleIndex ]:
            return middleIndex
        else:
            if self.target > self.nums[ middleIndex ]:
                return self._normalDichotomy( middleIndex + 1, end )
            else:
                return self._normalDichotomy( start, middleIndex )
