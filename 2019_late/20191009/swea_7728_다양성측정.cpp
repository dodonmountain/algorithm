#include <stdio.h>


int diversity(int num)
{
    int result = 0;
    int check_lst[10] = {0,};
    int tmp;
    while(num)
    {
        tmp = num % 10;
        check_lst[tmp] = 1;
        num = num / 10;
    }
    for(int i = 0;i<10;i++){
        result = result + check_lst[i];
    }
    return result;
}

int main()
{
    int T;
    int N;
    scanf("%d", &T);
    for(int t_case=1;t_case<T+1;t_case++){
        scanf("%d", &N);
        printf("#%d %d\n",t_case,diversity(N));
    }
    return 0;
}
