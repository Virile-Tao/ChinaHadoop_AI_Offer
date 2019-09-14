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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0) return NULL;
        int n = lists.size() - 1;
        while (n)
        {
            int i = 0;
            int j = n;
            while (i<j)
            {
                lists[i] = mergeList(lists[i], lists[j]);
                i++;
                j--;
            }
            n /= 2;
        }
        return lists[0];
    }
    ListNode* mergeList(ListNode* l1, ListNode* l2)
    {
        ListNode* dummy = new ListNode(0);
        ListNode* cur = dummy;  
        while (l1 && l2)
        {
            if (l1->val <= l2->val) 
            {
                cur->next = l1;
                cur = l1;
                l1 = l1->next;
            }
            else
            {
                cur->next = l2;
                cur = l2;
                l2 = l2->next;
            }
        }
        if (l1 == NULL) cur->next = l2;
        if (l2 == NULL) cur->next = l1;
        return dummy->next;
    }
};
