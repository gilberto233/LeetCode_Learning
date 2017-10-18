class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        strs.sort(key=lambda x: len(x), reverse=True)

        for index, word1 in enumerate( strs ):
            if all( not self._isSubWord( word1, word2 ) for subIndex, word2 in enumerate( strs ) if index != subIndex ):
                return len( word1 )
        return -1

    def _isSubWord(self, word1, word2):
        index = 0
        for character in word2:
            if index < len( word1 ) and word1[ index ] == character:
                index += 1

        return ( index == len( word1 ) )
        
