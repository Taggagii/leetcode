#include <iostream>
#include <bitset>

using namespace std;

// class Solution {
// public:
//     uint32_t reverseBits(uint32_t n) {
//         uint32_t output = 0;
//         for (int i = 0; i < 31; ++i) {
//             uint32_t temp = n & 1; // get the bit at the end of the thing
//             // now shift the output to the right to expose the next value
//             n >>= 1;
//             // put that bit into output by ORing it with temp
//             output |= temp;
//             // now we have that bit in the first position, we need to shift it left now
//             output <<= 1;
//         }
//         return output;
//     }
// };

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t output = 0;
        while (n > 0) {
            output <<= 1;
            output |= n & 1;
            n >>= 1;
        }
        return output;
    }
};


int main() {
    Solution* solution = new Solution();
    uint32_t value = solution->reverseBits(43261596);
    bitset<32> x(value);
    bitset<32> y(43261596);
    cout << y << endl;
    cout << x << endl;
}