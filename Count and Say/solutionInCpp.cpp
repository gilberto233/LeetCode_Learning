class Solution {
public:
    string countAndSay(int n) {
        return _recursion(n);
    }
    
    
private:
    string _recursion(int level) {
        string buffer, result = "";
        if (level == 1) return "1";
        else {
            buffer = _recursion(level - 1);
            char prevChar = buffer[0];
            int count = 0, i;

            for (i = 0; i<buffer.length(); ++i) {
                if (buffer[i] != prevChar) {
                    result += '0' + count;
                    result += prevChar;
                    prevChar = buffer[i];
                    count = 0;
                }
                ++count;
            }
            if (buffer[i-1] == prevChar) {
                result += '0' + count;
                result += prevChar;
            }

        }

	    return result;
    }
};
