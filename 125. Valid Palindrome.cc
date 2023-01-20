#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
private:
    static bool valid(char c) {
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9');
    }

    static bool charEqual(char a, char b) {
        return tolower(a) == tolower(b);
    }
public:
    bool isPalindrome(string s) {
        // check with the string processing within it
        string::iterator start = s.begin();
        string::iterator end = s.end();

        while (start < end) {
            bool invalidStart = !valid(*start);
            bool invalidEnd = !valid(*end);
            if (invalidStart || invalidEnd) {
                start += invalidStart;
                end -= invalidEnd;
                continue;
            }

            if (!charEqual(*start, *end)) {
                return false;
            }
            ++start;
            --end;
        }
        
        return true;



        // // remove all non-alphanumeric characters
        // s.erase(remove_if(s.begin(), s.end(), this->isNotAlphanumeric), s.end());
        // // convert uppercase to lowercase
        // transform(s.begin(), s.end(), s.begin(), [](unsigned char c){ return tolower(c); });

        // cout << s << endl;

        // // check if palindrome
        // // put an iterator at the beginning and the end and return false if they're ever not the same
        // string::iterator start = s.begin();
        // string::iterator end = s.end();

        // while (start < end) {
        //     if (*start != *end) {
        //         return false;
        //     }
        // }
        
        // return true;        
    }



};

int main() {
    Solution* solution = new Solution();
    cout << solution->isPalindrome("A man, a plan, a canal: Panama") << endl;
    cout << solution->isPalindrome("0P") << endl;
}