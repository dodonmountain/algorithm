#include <stdio.h>

int main()
{
    int T;
    int N;
    scanf("%d",&T);
    for (int t_case=1;t_case<T+1;t_case++){
        int arr[100] = {0,};
        int mind = 0;
        int maxd = 0;
        scanf("%d", &N);
        for (int i=0;i<N;i++){
            scanf("%d", &arr[i]);
        }
        for (int i=0;i<N-1;i++){
            if (arr[i + 1] - arr[i] > maxd){
                maxd = arr[i + 1] - arr[i];
            }
            if (arr[i + 1] - arr[i] < mind){
                mind = arr[i+1] - arr[i];
            }
        }
        printf("#%d %d %d\n",t_case, maxd, mind * -1);
    }
    return 0;
}
