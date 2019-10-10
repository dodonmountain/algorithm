#include <stdio.h>
#include <iostream>

int main()
{
    using namespace std;
    int T;
    int N;
    long tmp = 9999999999999;
    int distances[1001];
    int answer[2];
    scanf("%d", &T);
    for(int t_case = 1;t_case<=T;t_case++){
        std::fill_n(distances,1001,-100001);
        std::fill_n(answer,2,0);
        tmp = 9999999999999;
        scanf("%d", &N);
        for(int i =0;i<N;i++){
            scanf("%d", &distances[i]);
        }
        for(int i=0;i<N;i++){
            if(distances[i]<0 && distances[i] != -100001){
                distances[i] = -1 * distances[i];
            }
        }
        for(int i=0;i<N;i++){
            if(distances[i] <= tmp && distances[i] >= 0){
                if(distances[i]==tmp ){
                    answer[0] = answer[0] + 1;
                }else{
                    answer[0] = 1;
                    answer[1] = distances[i];
                    tmp = answer[1];
                }
            }
        }
        printf("#%d %d %d\n",t_case, answer[1], answer[0]);
    }
    return 0;
}
