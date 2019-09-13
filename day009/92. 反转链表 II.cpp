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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if (head == NULL) return head;
        if (m==n) return head;
        ListNode* pre = NULL;
        ListNode* cur = head;
        int tmp = m;
        while (tmp-1)
        {
            pre = cur;
            cur = cur->next;
            tmp--;
        }
        ListNode* p = cur->next;
        ListNode* q = p->next;
        while (n-m-1)
        {
            p->next = cur;
            cur = p;
            p = q;
            q = q->next;
            n--;
        }
        p->next = cur;
        if (pre != NULL)
        {
            pre->next->next = q;
            pre->next = p;
        }
        else
        {
            head->next = q;
            head = p;
        }
        return head;
    }
};
