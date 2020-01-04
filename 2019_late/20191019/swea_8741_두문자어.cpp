#include <iostream>
#include <string>


int main()
{
    using namespace std;
    int T;
    cin >> T;
    for(int tc=1;tc<T+1;tc++)
    {
        string a, b, c, ans;
        cin >> a;
        cin >> b;
        cin >> c;
        ans += toupper(a.front());
        ans += toupper(b.front());
        ans += toupper(c.front());
        cout<<'#'<<tc<<" "<<ans<<endl;
    }
    
    return 0;
}
