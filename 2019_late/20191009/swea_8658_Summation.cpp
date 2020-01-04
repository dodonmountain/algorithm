#include <stdio.h>

int div(int num)
{
    int result = 0;
    while(num)
    {
        result = result + (num % 10);
        num = num / 10;
    }
    return result;
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int t_case = 1;t_case<=T;t_case++){
        int arr[10];
        int max_answer = 0;
        int min_answer = 500;
        for (int i=0;i<10;i++){
            scanf("%d", &arr[i]);
        }
        for(int i=0;i<10;i++)
        {
            int k = div(arr[i]);
            if(k > max_answer)
            {
                max_answer = k;
            }

            if(k < min_answer)
            {
                min_answer = k;
            }

        }
        printf("#%d %d %d\n",t_case,max_answer,min_answer);
    }
    return 0;
}
