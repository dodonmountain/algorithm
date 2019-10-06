#include<iostream>
using namespace std;
 
int main()
{
    int T;
    cin>>T;
    for(int t_case=1;t_case<=T;t_case++){
     
        int start,end,price;
        cin>>start>>end;
        price=0;
        while(start!=end){
            start++;
            if(6<start && start<=12)
                price+=100;
            else if(12<start && start<=18)
                price+=150;
            else if(18<start && start<=24)
                price+=200;
            else if(0<start && start<=6)
                price+=300;
            if(start==end)
                break;
            start = start % 24;

        }
        cout<<"#"<<t_case<<" "<<price<<endl;
         
    }
     
    return 0;
}
 