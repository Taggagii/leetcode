#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0;
        int mostElement = 0;
        for (auto value : nums) {
            if (count == 0) {
                mostElement = value;
            }

            if (mostElement == value) {
                ++count; 
            } else {
                --count;
            }
        }
        return mostElement;
    }
};


int main() {
    Solution* solution = new Solution();
    vector<int> testCase = {1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 1, 1};
    cout << solution->majorityElement(testCase) << endl;
}