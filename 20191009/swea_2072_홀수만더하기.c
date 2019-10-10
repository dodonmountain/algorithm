#include <stdio.h>

int main() {
    int t;
    scanf("%d",&t);
    for (int tc=1;tc<t+1;tc++){
        int res = 0;
        for(int i=0;i<10;i++){
            int tmp = 0;
            scanf("%d",&tmp);
            if (tmp & 1){
                res = res + tmp;
            }
        }
        printf("#%d %d\n",tc,res);
    }
    return 0;
}