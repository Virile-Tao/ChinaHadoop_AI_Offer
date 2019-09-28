class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n1 = s1.size();
        int n2 = s2.size();
        if (n1 > n2) return false;
        int s1_map[26] = {0};
        int s2_map[26] = {0};
        for (int i=0; i<n1; i++)
        {
            s1_map[s1[i]-'a']++;
            s2_map[s2[i]-'a']++;
        }
        for (int i=0; i<n2-n1; i++)
        {
            if (matches(s1_map, s2_map)) return true;
            s2_map[s2[i+n1]-'a']++;
            s2_map[s2[i]-'a']--;
        }
        return matches(s1_map, s2_map);
    }
    bool matches(int s1_map[], int s2_map[])
    {
        for (int i=0; i<26; i++)
        {
            if (s1_map[i] != s2_map[i]) return false;
        }
        return true;
    }
};
