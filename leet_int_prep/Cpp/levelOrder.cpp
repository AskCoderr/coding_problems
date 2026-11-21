struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> resultVec;

        if (root == nullptr) {
            return resultVec;
        }

        int counter = 0;
        int numNodesInLevel = 1;
        int numNodesInNextLevel = 0;
        vector<int> tempVec;
        queue<TreeNode*> que;
        que.push(root);

        while (!que.empty()) {
            while (counter != numNodesInLevel) {
                tempVec.push_back(que.front()->val);
                if (que.front()->left) {
                    que.push(que.front()->left);
                    numNodesInNextLevel++;
                }
                if (que.front()->right) {
                    que.push(que.front()->right);
                    numNodesInNextLevel++;
                }

                que.pop();
                counter++;
            }
            counter = 0;
            numNodesInLevel = numNodesInNextLevel;
            numNodesInNextLevel = 0;
            resultVec.push_back(tempVec);
            tempVec.clear();
        }

        return resultVec;
    }
};

/*
IDEA

add root node to queue initially

assign current level node values from queue to level array while removing one from node counter for current level
    while doing that count the valid left and right nodes of each of the arrays in current level in nextCounter and assign those nodes in queue

at the end of iteration assign the array to result array and empty the temporary array


ALGORITHM
counter = 0
numNodesinLevel = 1
numNodesinNextLevel = 0
tempVec = {}
resultVec = {}
queue = {root}

while queue not empty
    while counter != numNodesinLevel:
        read front node value in queue and assign to tempVec
        if left exists
            add to queue
            add to numNodesinNextLevel
        if right exists
            add to queue
            add to numNodesinNextLevel

        pop from queue
        counter++
    
    counter = 0
    numNodesinLevel = numNodesinNextLevel
    numNodesinNextLevel = 0
    resultVec.pushback(tempVec)
    tempVec.clear()

return resultVec;
*/

// https://leetcode.com/problems/binary-tree-level-order-traversal/