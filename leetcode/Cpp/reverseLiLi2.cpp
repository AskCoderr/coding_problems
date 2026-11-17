#include <iostream>

// Definition for singly-linked list.

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
    ListNode *reverseBetween(ListNode *head, int left, int right)
    {
        if (right - left == 0)
        {
            return head;
        }

        ListNode *temp = head;
        int index = 1;
        if (left != 1)
        {
            while (index != (left - 1))
            {
                temp = temp->next;
                ++index;
            }
        }

        ListNode *temp2 = nullptr;
        if (left == 1)
        {
            temp2 = head;
        }
        else
        {
            temp2 = temp->next;
        }

        ListNode *reversed = nullptr;
        ListNode *reversedEnd = reversed;
        ListNode *newNode = nullptr;
        if (left != 1)
        {
            ++index;
        }
        int tempIndex = index;
        while (index != (right + 1))
        {
            if (index == (tempIndex + 1))
            {
                reversedEnd = reversed;
            }
            newNode = new ListNode(temp2->val, reversed);
            reversed = newNode;
            temp2 = temp2->next;
            ++index;
        }

        if (left != 1)
        {
            temp->next = reversed;
        }
        else
        {
            head = reversed;
        }
        // some error here i assume
        reversedEnd->next = temp2;

        return head;
    }
};

int main()
{
    // ListNode *liLi = new ListNode(1, new ListNode(2, (new ListNode(3, new ListNode(4, new ListNode(5))))));
    ListNode *lili = new ListNode(5, new ListNode(4, new ListNode(3, new ListNode(2))));
    Solution sol;
    ListNode *head = sol.reverseBetween(lili, 3, 4);
    while (head != nullptr)
    {
        std::cout << head->val << '\n';
        head = head->next;
    }
    return 0;
}

// https://leetcode.com/problems/reverse-linked-list-ii/description//
