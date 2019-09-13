/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        if (head == NULL) return head;
        while (head && head->val == val) head = head->next;
        if (head == NULL) return head;
        ListNode* p = head;
        ListNode* cur = p->next;
        while (cur)
        {
            if (cur->val == val)
            {
                p->next = cur->next;
                cur = cur->next;
            }
            else
            {
                p = cur;
                cur = cur->next;
            }
        }
        return head;
    }
};
