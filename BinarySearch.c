// Binary Search Example
// It must be done in ascending ordered array/list
// We can do it either recursively or repeatedly
#include <iostream>
#include <string>

int doBinarySearch(int arr[], int fetch, int left, int right)
{
    
    while(left <= right)
    {
        int midpoint = left + ((right - left) / 2);
    
        if(arr[midpoint] == fetch)
        {
            return fetch;   
        }
        else if(fetch < arr[midpoint])
        {
            right = midpoint - 1;
            //return doBinarySearch(arr, fetch, left, midpoint - 1);   
        }
        else if(fetch > arr[midpoint])
        {
            left = midpoint + 1;
            //return doBinarySearch(arr, fetch, midpoint+1, right);   
        }
    }
    
    return -1;
}


int main()
{
  int arr[] = {1,2,3,4,5};
  int fetch = 5;
  
  int result = doBinarySearch(arr, fetch, 0, sizeof(arr)/sizeof(arr[0]));
  
  printf("%d",result);
}