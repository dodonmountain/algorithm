#include<stdio.h>

int main()
{
    int T;
    scanf("%d", &T);
    for (int t_case=1; t_case<T+1; t_case++)
    {
        int student[1000] = {0,};
        int scores[101] = {0,};
        int tc;
        int tmp = 0;
        int max = 0;
        scanf("%d", &tc);
        for (int i = 0; i < 1000; i++){
            scanf("%d", &student[i]);
        }
        for (int i = 0; i < 1000; i++){
            scores[student[i]]++;
        }
        for (int i = 100; i > -1; i--){
            if (scores[i] > tmp){
                tmp = scores[i];
                max = i;
            }
        }
        printf("#%d %d\n",tc, max);
    }
    return 0;
}