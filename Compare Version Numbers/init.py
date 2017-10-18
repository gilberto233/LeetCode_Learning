from locale import atoi
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1Buffer = [ atoi( element ) for element in version1.split('.') ]
        version2Buffer = [ atoi( element ) for element in version2.split('.') ]

        index = 0
        len1 = len( version1Buffer )
        len2 = len( version2Buffer )
        while True:
            if ( not index < len( version1Buffer ) and ( not index < len( version2Buffer ) ) ):
                return 0
            if not index < len( version1Buffer ):
                version1Buffer.append(0)
            elif not index < len( version2Buffer ):
                version2Buffer.append(0)

            if version1Buffer[ index ] > version2Buffer[ index ]:
                return 1
            elif version2Buffer[ index ] > version1Buffer[ index ]:
                return -1
            else:
                index += 1
