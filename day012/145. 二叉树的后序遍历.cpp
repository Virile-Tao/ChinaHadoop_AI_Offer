/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        stack<TreeNode*> s1;
        stack<TreeNode*> s2;
        vector<int> res;
        TreeNode* tmp;
        if (root == NULL) return res;
        s1.push(root);
        while (!s1.empty())
        {
            tmp = s1.top();
            s1.pop();
            s2.push(tmp);
            if (tmp->left) s1.push(tmp->left);
            if (tmp->right) s1.push(tmp->right);
        }
        while (!s2.empty())
        {
            res.push_back(s2.top()->val);
            s2.pop();
        }
        return res;
    }
};
