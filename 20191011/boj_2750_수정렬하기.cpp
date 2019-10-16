#include <stdio.h>

void Swap(int arr[], int a, int b)
{
    int temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp;
}

int Partition(int arr[], int left, int right)
{
    int pivot = arr[left];
    int low = left + 1;
    int high = right;
 
    while (low <= high) 
    {
        while (pivot >= arr[low] && low <= right) 
        {
            low++; 
        }
        while (pivot <= arr[high] && high >= (left+1) )
        {
            high--;
        }
        if (low <= high)
        {
            Swap(arr, low, high);
        }
    }
    Swap(arr, left, high);
    return high;
 
}
 
void QuickSort(int arr[], int left, int right)
{
    if (left <= right)
    {
        int pivot = Partition(arr, left, right); 
        QuickSort(arr, left, pivot - 1);
        QuickSort(arr, pivot + 1, right); 
    }
}

int main()
{
    int N;
    int arr[10000000];
    scanf("%d",&N);
    for (int i = 0;i < N;i++){
        scanf("%d",&arr[i]);
    }
    QuickSort(arr, 0, N-1);
    for (int i = 0; i < N; i++){
        printf("%d\n",arr[i]);
    }
    return 0;
}
