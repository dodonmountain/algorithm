#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h> 

int main(void)
{
	int test_case;
	int T;
	setbuf(stdout, NULL);
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case)
	{
        char num[100001] = {0,};
        bool arr[10] = {false,};
        int cnt = 0;
        scanf("%s", num);
        for (int i=0;i<sizeof(num)/sizeof(int);i++){
            if (arr[num[i]-48]){
                arr[num[i]-48] = false;
            }
            else {
                arr[num[i]-48] = true;
            }
        }
        for (int i=0;i<10;i++){
            if (arr[i]){
                cnt = cnt + 1;
            }
        }
        printf("#%d %d\n",test_case,cnt);


	}
	return 0;
}