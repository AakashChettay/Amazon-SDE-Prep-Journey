#include <vector>
using namespace std;
class Solution {
public:
    vector<int> divisors(int n) {
        vector<int> v;
        for(int i=1; i<n+1; i++)
        {
            if(n%i==0)
                v.push_back(i);
        }
        return v;
    }
};