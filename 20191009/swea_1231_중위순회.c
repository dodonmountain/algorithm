#include <stdio.h>

int L[200];
int R[200];
char words[200];

void inorder(int v)
{
    if (v==0){
        return;
    }
    inorder(L[v]);
    printf("%c", words[v]);
    inorder(R[v]);
}

int main()
{
    for (int t_case = 1;t_case < 11; t_case++)
    {
        int V,p,l,r;      
        char w;
        scanf("%d",&V);
        for (int i = 1; i <= V; i++)
        {
            scanf("%d %c",&p, &w);
            words[p] = w;
            if ((p * 2) + 1 <= V)
            {
                scanf("%d %d", &L[p], &R[p]);
            }
            else if (p * 2 <= V) 
            {
                scanf("%d", &L[p]);
            }
        }
        printf("#%d ", t_case);
        inorder(1);
        printf("\n");
        for (int i = 0; i < V + 1; i++){
            words[i] = '0';
            L[i] = 0;
            R[i] = 0;
        }
        
    }
    return 0;
}