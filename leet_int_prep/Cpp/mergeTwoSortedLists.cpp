/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode result(0);
        ListNode* traveller = &result;
        int temp;

        while (true) {
            if (list1 == nullptr) {
                traveller->next = list2;
                return result.next;
            } else if (list2 == nullptr) {
                traveller->next = list1;
                return result.next;
            }

            if (list1->val <= list2->val) {
                temp = list1->val;
                list1 = list1->next;
            } else {
                temp = list2->val;
                list2 = list2->next;
            }
            traveller->next = new ListNode(temp);
            traveller = traveller->next;
        }
        return result.next;
    }
};


/*
- keep pointer a and b for lili a and b
- if pointer a is null append pointer b to resultant and return resultant
- if pointer b is null append pointer a to resultant and return resultant
- check which is lesser and append that to resultant lili and incremenet resultant pointer and a/b pointer
*/