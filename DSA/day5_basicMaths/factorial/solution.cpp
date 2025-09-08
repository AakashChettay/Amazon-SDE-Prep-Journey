class Solution {
public:
    int factorial(int n) {
        if(n == 1 || n == 0)
            return 1;
        return n * factorial(n-1);
    }
};

void main()
{
    int n;
    cin>>n;
    Solution obj;
    cout<<obj.factorial(n);
}