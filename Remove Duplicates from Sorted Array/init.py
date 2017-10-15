class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        
        while index < len( nums ):
            if len( nums ) == 1:
                return len( nums )
            if nums[ index ] == nums[ index - 1 ]:
                nums.remove( nums[ index ] )
            else:
                index += 1

        return len( nums )
    
    def solutionByGoogle(self, A):
        if not A:
            return 0

        newTail = 0

        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]

        return newTail + 1
        
