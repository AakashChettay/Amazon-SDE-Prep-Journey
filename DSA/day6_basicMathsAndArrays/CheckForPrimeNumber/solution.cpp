#include <cmath>
class Solution {
public:
    bool isPrime(int n) {
        if(n==1) return false;
        for(int i=2; i <= (int) pow(n, 0.5); i++)
        {
            if(n%i==0)
                return false;
        }
        return true;
    }
};