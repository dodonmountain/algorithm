#include<stdio.h>

int main(){
    int T;
    scanf("%d", &T);
    for (int tc = 0; tc < T; tc++)
    {
        int N;
        int ops[4];
        int arr[12];
        scanf("%d", &N);
        for (int i = 0; i < 4; i++) {
            scanf("%d",ops[i]);
        }
        for (int i = 0; i < N; i++) {
            scanf("%d",arr[i]);
        }
        
    }
    
    return 0;
}