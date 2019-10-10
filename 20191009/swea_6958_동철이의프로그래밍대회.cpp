#include <stdio.h>

int main()
{
    int T;

    scanf("%d", &T);
    for(int t_case=1;t_case<T+1;t_case++)
    {
        int M;
        int N;
        int maxnow = 0;
        int arr[20][20];
        int cnt = 0;
        scanf("%d %d",&N, &M);
        for(int j=0;j<N;j++)
        {
            int tmp = 0;
            for(int i=0;i<M;i++)
            {
                scanf("%d",&arr[j][i]);
                tmp = tmp + arr[j][i];
            }
            if(tmp>=maxnow){
                if(tmp == maxnow){
                    cnt = cnt + 1;
                }
                else{
                    cnt = 1;
                    maxnow = tmp;
                }
            }
        }
        printf("#%d %d %d\n",t_case,cnt,maxnow);
    }
    return 0;
}
