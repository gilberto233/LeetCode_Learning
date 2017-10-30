class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.target = target
        self.nums = nums

        index = self._dichotomy2( 0, len( nums ) )
        if index is -1:
            return [ -1, -1 ]
        else:
            startpoint, endpoint = index, index
            while startpoint > 0 and self.nums[ startpoint - 1 ] == self.target:
                startpoint -= 1
            while endpoint < len( self.nums ) - 1 and self.nums[ endpoint + 1 ] == self.target:
                endpoint += 1

            return [ startpoint, endpoint ]

    def _dichotomy2(self, start, end):
        try:
            middleIndex = start + int( ( end - start ) / 2 )
            if self.nums[ middleIndex ] == self.target:
                return middleIndex
            else:
                if start is end:
                    return -1
                elif self.nums[ middleIndex ] > self.target:
                    return self._dichotomy2( start, middleIndex )
                elif self.nums[ middleIndex ] < self.target:
                    return self._dichotomy2( middleIndex + 1, end )
        except IndexError:
            return -1

            
