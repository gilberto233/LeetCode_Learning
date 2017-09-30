class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        group_by_row = {}
        for index in range(numRows):
            group_by_row[index] = ''

        index = 0
        direction = 0
        cnt = 0
        while index < len( s ):
            group_by_row[ cnt ] += s[ index ]

            if cnt == numRows - 1 or cnt == 0:
                direction = not direction

            if numRows == 1:
                pass
            elif direction:
                cnt += 1
            else: cnt -= 1

            index += 1

        result = ''
        for element in group_by_row.values():
            result += element

        return result
