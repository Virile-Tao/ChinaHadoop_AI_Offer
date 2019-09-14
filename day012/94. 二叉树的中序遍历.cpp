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
    vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode*> s;
        vector<int> res;
        TreeNode* tmp;
        while (root)
        {
            s.push(root);
            root = root->left;
        }
        while (!s.empty())
        {
            tmp = s.top();
            s.pop();
            res.push_back(tmp->val);
            tmp = tmp->right;
            while (tmp)
            {
                s.push(tmp);
                tmp = tmp->left;
            }
        }
        return res;
    }
};
