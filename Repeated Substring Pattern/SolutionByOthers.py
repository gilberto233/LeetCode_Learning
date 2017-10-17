    def solutionByOthers(self, s):
        if not s:
            return False
        
        mirror = ( s + s )[ 1: -1 ]
        if s in mirror:
            return True
        else:
            return False
