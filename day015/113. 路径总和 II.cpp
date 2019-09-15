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
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int> > res;
        vector<int> tmp;
        helper(root, sum, res, tmp);
        return res;
    }
    void helper(TreeNode* root, int sum, vector<vector<int> >& res, vector<int> tmp)
    {
        if (root == NULL) return ;
        if (root->left == NULL && root->right == NULL && root->val == sum)
        {
            tmp.push_back(root->val);
            res.push_back(tmp);
            return ;
        }
        tmp.push_back(root->val);
        helper(root->left, sum - root->val, res, tmp);
        helper(root->right, sum - root->val, res, tmp);
    }
};
