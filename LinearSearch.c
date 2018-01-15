// Example program
#include <iostream>
#include <string>

int doLinearSearch(int arr[],int fetch,int size)
{
    for(int i = 0 ; i < size ; i++)
    {
        if(arr[i] == fetch)
        {
            return fetch;
        }
        
    }
    
    return -1;
}


int main()
{
  int arr[] = {1,2,3,4,5};
  int fetch = 3;
  
  int result = doLinearSearch(arr, fetch, sizeof(arr)/sizeof(arr[0]));
  
  printf("%d",result);
}