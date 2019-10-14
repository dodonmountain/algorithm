#include<stdio.h>

int main()
{
    int T;
    scanf("%d", &T);
    for (int tc=1;tc<T+1;tc++)
    {
        int L, U, X;
        int res;
        scanf("%d %d %d", &L, &U, &X);
        if (X > U)
        {
            res = -1;
        }
        else if (X >= L)
        {
            res = 0;
        }
        else
        {
            res = L - X;
        }
        printf("#%d %d\n", tc, res);

    }
}