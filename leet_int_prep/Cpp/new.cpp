#include <vector>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        
    }
};

/*
IDEA

- check if it belongs to rotated or unrotated group, by comparing to the
    first element of the array

- if in rotated, top pointer at end and bottom pointed at start of the array and
    compare the top pointer always to the target variable

- else, do same but compare the bottom pointer

- now during comparison we should keep track of the previous node we jumped from,
    cause in case if the value newly compared asks to, then we have to move back

- if greater than bottom pointer move the bottom pointer, else go back to
    previous node and move the bottom pointer again

- if is target return the index and be happy

- if (top-bottom) == 1: then return -1

ALGORITHM



if array[0] == target return 0
rotated = target > array[0] ? true : false


*/

// https://leetcode.com/problems/search-in-rotated-sorted-array/description/