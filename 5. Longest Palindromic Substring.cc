#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {

        float length = 0;
        float index = 0;

        for (int i = 0; i < s.length(); ++i) {
            int len1 = expandFromMiddle(s, i, i);
            int len2 = expandFromMiddle(s, i, i + 1);
            int curLength = max(len1, len2);
            if (curLength > length) {
                length = curLength;
                index = i;
            }
        }

        int start = index - (int)((length - 1) / 2);

        return s.substr(start, length);
    }

    int expandFromMiddle(string s, int left, int right) {
        int length = s.length();
        while (left >= 0 && right < length && s[left] == s[right])
        {
            left--;
            right++;
        }

        return right - left - 1;
    }
};

int main()
{
    Solution* sol = new Solution();
    string s = "cbbaqwerqa";
    cout << sol->longestPalindrome(s) << endl;
}