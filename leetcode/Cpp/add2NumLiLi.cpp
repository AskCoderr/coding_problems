#include <iostream>

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode *result = nullptr;
        
        ListNode *temp1 = l1;
        ListNode *temp2 = l2;
        ListNode *temp3 = result;
        bool carry = false;
        
        // so first create the result node then do the summation, if carry add 1, check if sum > 10, if yes then carry true else false
        while (temp1 != nullptr && temp2 != nullptr) {
            ListNode *node = new ListNode();
            int sum = temp1->val + temp2->val;
            
            if (carry) {
                ++sum;
            }
            if (sum >= 10) {
                sum = sum % 10;
                carry = true;
            } else {
                carry = false;
            }

            node->val = sum;

            if (temp3 == nullptr) {
                temp3 = node;
                result = temp3;
            } else {
                temp3->next = node;
                temp3 = temp3->next;
            }

            temp1 = temp1->next;
            temp2 = temp2->next;
        }


        // select the pointer that has not ended, create the result node, then if carry, if nodeval == 9, val = 0, carry true else val = nodeval, carry false
        if (temp2 != nullptr) {
            temp1 = temp2;
        }

        while (temp1 != nullptr) {
            ListNode *node = new ListNode();
            
            if (carry) {
                if (temp1->val == 9) {
                    node->val = 0;
                } else {
                    node->val = temp1->val+1;
                    carry = false;
                }
            } else {
                node->val = temp1->val;
            }
            temp3->next = node;
            temp3 = temp3->next;
            temp1 = temp1->next;
        }
        if (carry) {
            temp3->next = new ListNode(1);
        }

        return result;
    }
};

int main() {
    ListNode *l1 = new ListNode(1, new ListNode(0, new ListNode(0, new ListNode(4))));
    ListNode *l2 = new ListNode(5, new ListNode(6, new ListNode(4)));

    Solution solution = Solution();
    ListNode *ans = solution.addTwoNumbers(l1, l2);
    while (ans != nullptr) {
        std::cout << ans->val << " ";
        ans = ans->next;
    }
}

// https://leetcode.com/problems/add-two-numbers/
