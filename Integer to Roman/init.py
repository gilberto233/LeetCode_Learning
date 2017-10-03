class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ''

        T = int( num / 1000 )
        result += T * 'M'
        num %= 1000

        H = int( num / 100 )
        if H < 4: result += H * 'C'
        elif H == 4: result += 'CD'
        elif H > 4 and H < 9: result += 'D' + ( H - 5 ) * 'C'
        else: result += ( 10 - H ) * 'C' + 'M'
        num %= 100

        Te = int( num / 10 )
        if Te < 4: result += Te * 'X'
        elif Te == 4: result += 'XL'
        elif Te > 4 and Te < 9: result += 'L' + ( Te - 5 ) * 'X'
        else: result += ( 10 - Te ) * 'X' + 'C'
        num %= 10

        if num < 4: result += num * 'I'
        elif num == 4: result += 'IV'
        elif num > 4 and num < 9: result += 'V' + ( num - 5 ) * 'I'
        else: result += ( 10 - num ) * 'I' + 'X'

        return result
