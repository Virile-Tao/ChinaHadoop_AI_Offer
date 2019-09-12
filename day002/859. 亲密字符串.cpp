class Solution {
public:
    bool buddyStrings(string A, string B) {
        int i = 0, j = 0;
        int n = A.size(), m = B.size();
        if (n != m) return false;
        while (i<n && A[i] == B[j])
        {
            i++;
            j++;
        }
        if (i == n) //此时情况比较麻烦，A和B一样
        {
            map<char,int> m;
            for (char c : A)
            {
                if (m.find(c) == m.end()) m[c] = 1;
                else m[c]++;
            }
            for(map<char,int>::iterator it=m.begin(); it!=m.end(); it++)
            {
                if (it->second > 1) return true;
            }
            return false;
        }
        while (i<n && A[i] != B[j]) j++;
        if (j==n) return false;
        if (A[i] == B[j] && A[j] == B[i])
        {
            j++;
            while (j<n && A[j] == B[j]) j++;
            if (j==n) return true;
            else return false;
        }
        else return false;
    }
};
