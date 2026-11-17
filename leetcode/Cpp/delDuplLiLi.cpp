// * Definition for singly-linked list.
#include <unordered_set>

using std::unordered_set;

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
    unordered_set<int> set;
    ListNode *deleteDuplicates(ListNode *head)
    {
        if (head == nullptr)
        {
            return head;
        }

        ListNode *temp = head;
        set.insert(temp->val);

        while (temp->next != nullptr)
        {
            if (set.count((temp->next)->val))
            {
                temp->next = temp->next->next;
            }
            else
            {
                set.insert(temp->next->val);
                temp = temp->next;
            }
        }
        return head;
    }
};

// https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/