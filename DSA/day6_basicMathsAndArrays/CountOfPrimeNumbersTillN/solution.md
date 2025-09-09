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
    int primeUptoN(int n) {
        int primeCount = 0;
        for(int i=1; i<n+1; i++)
        {
            if(isPrime(i))
            {
                primeCount++;
            }
        }
        return primeCount;
    }
};