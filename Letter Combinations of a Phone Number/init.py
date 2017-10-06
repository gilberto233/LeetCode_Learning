from copy import copy
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []

        mapping = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        result_af = []

        try:
            for element in mapping[digits[0]]:
                result.append(element)
        except IndexError:
            return []

        result_af = copy( result )
        for index in range(1, digits.__len__()):
            del result[:]
            for element in result_af:
                for new_element in mapping[digits[index]]:
                    result.append(element + new_element)
            result_af = copy( result )

        return result
    
