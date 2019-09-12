class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0) return "";
        string ans = strs[0];
        for (int i=1; i<strs.size(); i++)
        {
            ans = help(ans, strs[i]);
        }
        return ans;
    }
    string help(string& s1, string& s2)
    {
        int i=0;
        int j=0;
        string res;
        while (i<s1.size(), j<s2.size())
        {
            if (s1[i] != s2[j]) return res;
            res += s1[i];
            i++;
            j++;
        }
        return res;
    }
};
