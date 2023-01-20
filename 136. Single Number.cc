#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int storeBits = 0;
        for (int num : nums) {
            storeBits ^= num;
        }
        return storeBits;
    }
};

int main() {
    vector<int> nums = {4, 1, 2, 1, 2};
    Solution* solution = new Solution();
    cout << solution->singleNumber(nums) << endl;
}