class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0;
        int j = s.size() - 1;
        while (i < j)
        {
            if (i < j && isalnum(s[i]) && isalnum(s[j]))
            {
                if (tolower(s[i]) == tolower(s[j]))
                {
                    i++;
                    j--;
                }
                else return false;
            }
            else
            {
                while (i<j && !isalnum(s[i])) i++;
                while (i<j && !isalnum(s[j])) j--;
            }
        }
        return true;
    }
};
