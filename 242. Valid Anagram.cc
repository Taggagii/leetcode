#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        int length = s.length();
        if (length!= t.length()) {
            return false;
        }

        unordered_map<char, int> counters;

        for (int i = 0; i < length; ++i) {
            // for ever value in s i'll add to counters
            // for ever vlaue in t i'll remove from counters
            // if all values are 0, we know they are anagrams of each other
            counters[s[i]] = counters[s[i]] + 1;
            counters[t[i]] = counters[t[i]] - 1;
        }

        for (auto x : counters) {
            if (x.second) {
                return false;
            }
        }
        
        return true;

    }
};


int main() {
    string s = "anagram";
    string t = "nagaram";

    Solution* solution = new Solution();
    cout << solution->isAnagram(s, t) << endl;
}