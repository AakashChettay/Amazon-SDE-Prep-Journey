#include<cmath>
class Solution {
public:
    bool isArmstrong(int n) {
        int len = 0;
        int dum = n;
        while(dum!=0)
        {
            len++;
            dum = (int)dum/10;
        }
        int store = n;
        int arm = 0;
        while(n!=0)
        {
            int dig = n%10;
            arm += pow(dig, len);
            n = (int) n/10;
        }
        //cout<<len<<" "<<arm<<" "<<store<<"\n";
        return arm == store;
    }
};

void main()
{
    int n;
    cin>>n;
    Solution obj;
    cout<<obj.isArmstrong(n);
}