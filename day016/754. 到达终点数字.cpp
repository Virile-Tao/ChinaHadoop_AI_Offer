class Solution {
public:
    int reachNumber(int target) {
        if (target < 0) target = - target;
        int i = 0;
        for(;;)
        {
            int tmp = (i + i*i)/2 - target;
            if (tmp >= 0 && tmp%2 == 0) return i;
            i++;
        }
    }
};
