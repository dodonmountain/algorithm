using namespace std;
#include<iostream>
#include<string>
int main()
{
    string a, b,result;
    cin >> a >> b;
    if (a.size() > b.size())
    {
        string c;
        for (int i = 0; i < a.size() - b.size(); i++)
            c += '0';
        b = c + b;
    }
    else
    {
        string c;
        for (int i = 0; i < b.size() - a.size(); i++)
            c += '0';
        a = c + a;
    } 
    int cc = 0;
    while (a.size()!=0 && b.size() !=0)
    {
        int aa = a.back() - '0';int bb = b.back() - '0';
        int remain = (cc + aa + bb) % 10; 
        cc = (cc + aa + bb) / 10; 
        result = (char)(remain + '0') + result; 
        a.pop_back();
        b.pop_back();
    }
    if(cc) 
        result = (char)(cc+'0') + result;
    cout << result << endl;
    return 0;
}
