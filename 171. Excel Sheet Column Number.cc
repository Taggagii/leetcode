class Solution {
public:
    int titleToNumber(string columnTitle) {
        // note: it's like a base 26 number meaning, we can just do the conversion as such
        int multiple = 1;
        int sum = 0;
        for (int i = columnTitle.length() - 1; i >= 0; --i) {
            char value = columnTitle[i];
            sum += (value - 64) * multiple;

            multiple *= 26;
        }
        return sum;
    }
};