class Solution {
public:
    string reverseWords(string s) {
        int n = s.size();
        if (n==0) return "";
        int i = 0;
        stack<string> res;
        while (i<n)
        {
            while (i<n && s[i]==' ') i++; //此时找到了单词的第一个字母
            string tmp;
            while (i<n && s[i]!=' ') tmp+=s[i++]; //拼接第一个单词
            res.push(tmp);
        }
        string ans;
        while (!res.empty())
        {
            if (res.top() != "")
            {
                ans += res.top();
                ans += ' ';
            }
            res.pop();
        }
        return ans.size() ? string(ans.begin(), ans.end()-1) : "";
    }
};
