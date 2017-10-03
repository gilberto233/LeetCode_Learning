class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        index = 0

        if s[0] == 'M':
            while index < len( s ):
                if not s[ index ] == 'M': break
                index += 1
            result += index * 1000

        start_point = index
        while index < len( s ):
            if not ( s[ index ] in 'DCM' ): break
            index += 1
        hundread_level = s[ start_point: index ]
        if hundread_level == '':
            pass
        elif hundread_level[0] == 'D':
            result += hundread_level.count( 'C' ) * 100 + 500
        elif hundread_level[ len( hundread_level ) - 1 ] == 'D':
            result += ( 500 - 100 * hundread_level.count( 'C' ) )
        elif hundread_level[ len( hundread_level ) - 1 ] == 'M':
            result += 900
        else: result += hundread_level.count( 'C' ) * 100

        start_point = index
        while index < len(s):
            if not (s[index] in 'LXC'): break
            index += 1
        ten_level = s[start_point: index]
        if ten_level == '':
            pass
        elif ten_level[0] == 'L':
            result += ten_level.count('X') * 10 + 50
        elif ten_level[len(ten_level) - 1] == 'L':
            result += (50 - 10 * ten_level.count('X'))
        elif ten_level[len(ten_level) - 1] == 'C':
            result += 90
        else: result += ten_level.count('X') * 10

        single_level = s[ index: len( s ) ]
        if single_level == '':
            pass
        elif single_level[0] == 'V':
            result += single_level.count('I') * 1 + 5
        elif single_level[len(single_level) - 1] == 'V':
            result += (5 - 1 * single_level.count('I'))
        elif single_level[len(single_level) - 1] == 'X':
            result += 9
        else: result += single_level.count('I')

        return result
