class Solution {
public:
    int reverse(int x) {
         
        long r = 0;
        int last_digit = 0;
        while(x)
        {
            last_digit = x%10;
            r = r*10 + last_digit;
            x = x/10;
        }
        if(r>INT_MAX || r<INT_MIN) return 0;
        return int(r);

    }
};