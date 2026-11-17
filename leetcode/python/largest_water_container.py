# be creative with the list brov use some crazy smart things now come on!!!
class Solution:
    def maxArea(self, height: list[int]) -> int:
        # variable to keep track of the already matched pairs of values from height
        connection_var = {}

        for i in range(len(height)):
            connection_var[i] = []

        def connect_assis(g, h):  # g and h are indexes of values from height
            connection_var.get(g).append(h)

        def area(lent, bret):
            return lent * bret


Solution().maxArea([6, 4, 7, 8, 7, 2, 3, 1, 7, 8, 2, 11, 4, 0])

# current plan is to have a system where we make sure each number gets associated with all the other numbers
# and there will be many efficient ways through which we check for the biggest container (bit hard to understand i know)

'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith 
line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water 
(blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''
