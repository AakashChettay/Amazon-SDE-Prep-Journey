1. Pascal Traingle<br><br>

a. 1st variation- Find r, c combination<br>
```
class Solution {
public:
    int pascalTriangleI(int r, int c) {
        long long ans = 1;
        int N = r-1, R = c-1; 
        for(int i=0; i<R; i++)
        {
            ans = ans * (N-i);
            ans = (int) ans / (i+1);
        }
        return ans;
    }
};
```
T.C: O(c)<br>
S.P: O(1)<br>
* To find it, we can use NcR formula, where N = r-1, R = c-1. To avoid huge factorial calculations using loops, we find an
  observation and implement logic based on it. (Running loop R times)<br><br>

b. 2nd variation, find entrire rth row.<br><br>

Better:<br>
```
class Solution {
public:
    int pascalTriangleI(int r, int c) {
        long long ans = 1;
        int N = r-1, R = c-1; 
        for(int i=0; i<R; i++)
        {
            ans = ans * (N-i);
            ans = (int) ans / (i+1);
        }
        return ans;
    }
    vector<int> pascalTriangleII(int r) {
        vector<int> ans;
        int N = r;
        for(int i = 1; i <= r; i++)
        {
            //cout<<N<<" "<<i<<endl;
            ans.push_back(pascalTriangleI(N, i));
        }
        return ans;
    }
};
```
T.C: O(r*c)
S.C: O(1) [As we don't count ans array]<br><br>

Optimal: 
```
class Solution {
public:
    vector<int> pascalTriangleII(int r) {
        vector<int> res;
        long long ans = 1;
        res.push_back(ans);
        for(int i=1; i<r; i++)
        {
            ans = ans * (r - i);
            ans = ans / i;
            res.push_back(ans);
        }
        return res;
    }
};
```
<img width="620" height="310" alt="image" src="https://github.com/user-attachments/assets/70ae1cd8-cb9a-4c1b-afb6-475d979a7dba" /><br><br>

T.C: O(r)<br>
S.C: O(1)


