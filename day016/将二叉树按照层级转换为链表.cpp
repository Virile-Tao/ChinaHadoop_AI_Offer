/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    /**
     * @param root the root of binary tree
     * @return a lists of linked list
     */
    vector<ListNode*> binaryTreeToLists(TreeNode* root) {
        // Write your code here
        vector<ListNode*> res;
        if (root == NULL) return res;
        std::queue<TreeNode*> q;
        q.push(root);
        int len;
        TreeNode* node;
        ListNode* dummy;
        ListNode* cur;
        while (!q.empty())
        {
            len = q.size();
            dummy = new ListNode(0);
            cur = dummy;
            while (len)
            {
                node = q.front();
                q.pop();
                len--; 
                cur->next = new ListNode(node->val);
                cur = cur->next;
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            res.push_back(dummy->next);
        }
        return res;
    }
};
