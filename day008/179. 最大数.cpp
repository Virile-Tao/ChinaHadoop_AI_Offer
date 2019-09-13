class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> s;
        for (int num: nums) s.push_back(to_string(num));
        sort(s.begin(), s.end(), cmp);
        if (s[0] == "0") return "0";
        string res;
        for (string i: s)  res += i;
        return res;
    }
    static bool cmp(string s1, string s2)
    {
        return s1 + s2 > s2 + s1;
    }
};
