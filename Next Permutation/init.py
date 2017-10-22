class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        endpoint = index = len( nums ) - 1

        if len( nums ) < 2:
            return

        while index > 0 and nums[ index ] <= nums[ index - 1 ]:
            index -= 1

        if index:
            buffer = nums.pop( index - 1 )
            subIndex = index
            while subIndex < endpoint and nums[ subIndex ] > buffer:
                subIndex += 1
            nums[ subIndex - 1 ], buffer = buffer, nums[ subIndex - 1 ]
            nums.insert( index - 1, buffer )

        while index < endpoint:
            nums[ index ], nums[ endpoint ] = nums[ endpoint ], nums[ index ]
            index += 1
            endpoint -= 1

        return
      
