class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> needs;
        unordered_map<char, int> window;
        for (char c : t) needs[c]++;
        int left = 0, right = 0;
        int matches = 0;
        int start = 0;
        int minLen = INT_MAX;
        while (right < s.size())
        {
            char ch = s[right];
            if (needs.count(ch))
            {
                window[ch]++;
                if (needs[ch] == window[ch]) matches++;
            }
            right++;
            while (matches == needs.size())
            {
                if (right - left < minLen)
                {
                    start = left;
                    minLen = right - left;
                }
                char tmp = s[left];
                if (needs.count(tmp))
                {
                    window[tmp]--;
                    if (window[tmp] < needs[tmp]) matches--;
                }
                left++;
            }
        }
        return minLen == INT_MAX ? "" : s.substr(start, minLen);
    }
};
