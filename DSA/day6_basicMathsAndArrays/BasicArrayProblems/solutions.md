**Sum of Array Elements**<br><br>
```
class Solution{
public:
	int sum(int arr[], int n) {
	int s = 0;
    for(int i=0; i<n; i++)
        s += arr[i];
    return s;
	}
};
```
**Count of Odd Numbers in Array**<br><br>
```
class Solution{
public:
    int countOdd(int arr[], int n){
          int count = 0;
          for(int i=0; i<n; i++)
          {
            if(arr[i]%2==1)
                count++;
          }
          return count;
    }
};
```
**Check if an Array is Sorted 1**<br><br>
```
class Solution {
public:
    bool arraySortedOrNot(int arr[], int n) {
        bool sorted = true;
        for(int i=0; i<n-1; i++)
        {
            if(arr[i] > arr[i+1])
                return false;
        }
        return true;
    }
};
```
**Reverse an Array**<br><br>
```
class Solution:
    def reverse(self, arr: list, n: int) -> None:
        left, right = 0, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

```