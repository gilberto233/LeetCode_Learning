class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        for index in range( nums.__len__() - 3 ):
            if index > 0 and ( nums[ index ] == nums[ index - 1 ] ):
                continue

            for sub_index in range( index + 1, nums.__len__() - 2 ):
                if sub_index > index + 1 and nums[ sub_index ] == nums[ sub_index - 1 ]:
                    continue
                startpoint, endpoint = sub_index + 1, nums.__len__() - 1

                while startpoint < endpoint:
                    buffer = []
                    totalSum = nums[ index ] + nums[ sub_index ] + nums[ startpoint ] + nums[ endpoint ]

                    if totalSum > target:
                        endpoint -= 1
                    elif totalSum < target:
                        startpoint += 1
                    else:
                        result.append( [ nums[ index ], nums[ sub_index ], nums[ startpoint ], nums[ endpoint ] ] )

                        while (startpoint < endpoint) and (nums[startpoint] == nums[startpoint + 1]):
                            startpoint += 1
                        while (startpoint < endpoint) and (nums[endpoint] == nums[endpoint - 1]):
                            endpoint -= 1
                        startpoint += 1
                        endpoint -= 1

        return result

    def solutionByOthers(self, nums, target):
        """
        This solution can handle every similar problem.
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []

        self._findNSum( nums, target, 4, [], results )
        return results

    def _findNSum( self, nums, target, N, result, results ):
        if len( nums ) < N or N < 2:
            return

        if N == 2:
            left, right = 0, len( nums ) - 1
            while left < right:
                if nums[ left ] + nums[ right ] == target:
                    results.append( result + [ nums[ left ], nums[ right ] ] )

                    left += 1
                    right -= 1
                    while left < right and nums[ left ] == nums[ left - 1 ]:
                        left += 1
                    while left < right and nums[ right ] == nums[ right + 1 ]:
                        right -= 1
                elif nums[ left ] + nums[ right ] < target:
                    left += 1
                else:
                    right -= 1
        else:
            for index in range( 0, len( nums ) - N + 1 ):
                if target < nums[ index ] * N or target > nums[ -1 ] * N:
                    break
                if index == 0 or index > 0 and nums[ index - 1 ] != nums[ index ]:
                    self._findNSum( nums[ index + 1: ], target - nums[ index ], N - 1, result + [ nums[ index ] ], results )

if __name__ == '__main__':
    data = []
    target = 0
    instance = Solution().solutionByOthers( data, target )
    print( instance )
