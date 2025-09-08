class Solution {
public:
    int largestDigit(int n) {
        if(n==0) return 0;
        int large = INT_MIN;
        while(n!=0)
        {
            int dig = n%10;
            if(dig > large)
                large = dig;
            n = (int) n/10;
        }
        return large;
    }
};

void main()
{
    int n;
    cin>>n;
    Solution obj;
    cout<<obj.largestDigit(n);
}