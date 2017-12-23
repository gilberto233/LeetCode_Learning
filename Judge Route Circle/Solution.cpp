class Solution {
public:
    bool judgeCircle(string moves) {
        int index = 0, upward = 0, downward = 0, leftward = 0, rightward = 0;

        while (moves[index] != '\0') {
            switch (moves[index]){
            case 'U':
                ++upward;
                break;
            case 'D':
                ++downward;
                break;
            case 'L':
                ++leftward;
                break;
            case 'R':
                ++rightward;
                break;
            default:
                    break;
            }

            ++index;
        }

        if ((upward == downward) && (leftward == rightward)) return true;
        else
		    return false;
    }
};
