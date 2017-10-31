class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not len( board ):
            return False
        row, column, block = [], [ [] for _ in range(9) ], [ [] for _ in range(3) ]

        for rowIndex in range(9):
            row.clear()
            if rowIndex % 3 is 0:
                block = [ [] for _ in range(3) ]

            for columnIndex in range(9):
                character = board[ rowIndex ][ columnIndex ]
                if not character is '.':
                    if not character in row:
                        row.append( character )
                    else:
                        return False
                    if not character in column[ columnIndex ]:
                        column[ columnIndex ].append( character )
                    else:
                        return False
                    if not character in block[ int( columnIndex / 3 ) ]:
                        block[ int( columnIndex / 3 ) ].append( character )
                    else:
                        return False

        return True
        
