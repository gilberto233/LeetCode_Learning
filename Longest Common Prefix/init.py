class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        index = 0

        if strs.__len__() is 0: return ''

        while True:
            try:
                buffer = strs[0][ index ]
                for sub_index in range( strs.__len__() ):
                    if not strs[ sub_index ][ index ] == buffer: return strs[0][ 0: index ]
                index += 1

            except IndexError: return strs[0][ 0: index ]
            
    def longestCommonPrefixByOthers(self, strs):
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)
            
