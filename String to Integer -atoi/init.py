class Solution(object):
    def myAtoi(self, istr):
        """
        :type istr: str
        :rtype: int
        """
        # integral, float, power
        str_buffer = istr.strip( ' ' )
        
        if not str_buffer.find( '-' ):
            sign = -1
            str_buffer = str_buffer[ 1: ] 
        else:
            if not str_buffer.find( '+' ): str_buffer = str_buffer[ 1: ] 
            sign = 1
           
        
        result = 0
        for element in str_buffer:
            if element in "1234567890":
                result = result * 10 + int( element )
            else: break

        result_sign = result * sign
        if result_sign > 2147483647: return 2147483647
        elif result_sign < -2147483648: return -2147483648
        else: return result_sign
