#include <vector>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        if (size(height) == 2) {
            return min(height[0], height[1]);
        }

        int l = 0, r = size(height)-1, max_area = (size(height)-1) * min(height[0], height[size(height)-1]);
        int max_ind_l = l;
        int max_ind_r = r;
        bool inc_left = (height[r] < height[l]) ? false : true;
        int temp;

        while (true) {
            if (inc_left) {
                l++;
                if (height[l] > height[max_ind_l]) {
                    inc_left = (height[r] < height[l]) ? false : true;
                    max_ind_l = l;
                    temp = (r-l) * min(height[l], height[r]);
                    max_area = (temp > max_area) ? temp : max_area;
                }
            } else {
                r--;
                if (height[r] > height[max_ind_r]) {
                    inc_left = (height[r] < height[l]) ? false : true;
                    max_ind_r = r;
                    temp = (r-l) * min(height[l], height[r]);
                    max_area = (temp > max_area) ? temp : max_area;
                }
            }

            if (r-l == 1) {
                break;
            }
        }

        return max_area;
    }
};

/*
IDEA

left and right pointers, max_area, max_len_and_index for left and right pointers
the bottleneck pointer searches for a index with more height
if the pointers have equal length then the left one moves forward

if we find a pointer with bigger height, 
    calculate the area, if area is bigger update max_area, 
    update max_len_and_ind as well and switch direction

if the distance between the pointer is one at the end of the loop
    then return max_area


PSUEDOCODE

l = 0, r = len(vector), max_area = 0, max_len_index_l = (0, height[0]), max_len_index_r = (len(vec)-1, height[len(vec)-1])
inc_left = false if right bar smaller

while true:
    if inc_left:
        l++
        if height[l] > max_len_index_l[1]:
            update inc_left
            update max_len_index_l
            update max_area
    
    if !inc_left:
        r--
        if height[r] > max_len_index_r[1]:
            update inc_left
            update max_len_index_r
            update max_area
    
    if r-l == 1:
        break

return max_area
*/

// https://leetcode.com/problems/container-with-most-water/