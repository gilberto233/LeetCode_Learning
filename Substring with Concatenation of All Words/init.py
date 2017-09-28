from copy import deepcopy
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        words_count = len( words )
        words_len = len( words[0] )
        total_length = words_count * words_len
        result = []

        index = 0
        while index < len( s ) - total_length:
            word_buffer = deepcopy( words )
            sub_string = s[ index: index + words_len ]
            if sub_string in words:
                word_buffer.remove( sub_string )

                for remain_word in range( 1, words_count ):
                    sub_string = s[ index + remain_word * words_len: index + words_len * ( remain_word + 1 ) ]
                    if sub_string in word_buffer:
                        word_buffer.remove( sub_string )

                if len( word_buffer ) == 0:
                    result.append( index )
                    index += total_length - 1

            index += 1

        return result

if __name__ == '__main__':
    s = 'barfoothefoobarman'
    L = [ 'foo', 'bar' ]
    instance = Solution().findSubstring( s, L )
    print( instance )

