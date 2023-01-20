#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> differenceToIndex;

        for (auto i = nums.begin(); i != nums.end(); ++i) {
            differenceToIndex[target - *i] = i - nums.begin();
        }

        for (auto i = nums.begin(); i != nums.end(); ++i) {
            auto found = differenceToIndex[*i];
            int index = i - nums.begin();
            if (found && found != index) {            
                return {found, index};
            }
        }

        return {};

    }
};


int main() {
    vector<int> nums = {1,3,4,2};

    Solution* solution = new Solution();
    vector<int> output = solution->twoSum(nums, 6);

    for (int i = 0; i < 10; ++i) {
        cout << '-';
    }
    cout << endl;

    for (auto x : output) {
        cout << x << endl;
    }

}