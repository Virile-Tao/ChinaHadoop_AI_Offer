/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
    TreeNode* sortedListToBST(ListNode* head) {
        vector<int> nums;
        while (head)
        {
            nums.push_back(head->val);
            head = head->next;
        }
        return helper(nums, 0, nums.size()-1);
    }
    TreeNode* helper(vector<int>& nums, int low, int high)
    {
        if (low > high) return NULL;
        int mid = (low + high) / 2;
        TreeNode* root = new TreeNode(nums[mid]);
        root->left = helper(nums, low, mid-1);
        root->right = helper(nums, mid+1, high);
        return root;
    }
};
