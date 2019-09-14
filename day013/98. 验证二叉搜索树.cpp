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
    bool isValidBST(TreeNode* root) {
        long tmp = LONG_MIN;
        bool res = true;
        helper(root, tmp, res);
        return res;
    }
    void helper(TreeNode* root, long& tmp, bool& res)
    {
        if (root == NULL) return ;
        helper(root->left, tmp, res);
        if (tmp >= root->val)
        {
            res = false;
            return ;
        }
        tmp = root->val;
        helper(root->right, tmp, res);
    }
};
