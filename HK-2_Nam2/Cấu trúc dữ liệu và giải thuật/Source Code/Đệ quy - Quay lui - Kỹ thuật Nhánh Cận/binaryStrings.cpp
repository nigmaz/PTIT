#include <iostream>
using namespace std;
int n, B[20];

void output()
{
    for (int i = 1; i <= n; i++)
        cout << B[i] << " ";
    cout << endl;
}

void Try(int i)
{
    for (int j = 0; j <= 1; j++)
    {
        B[i] = j;
        if (i == n)
            output();
        else
            Try(i + 1);
    }
}

int main()
{
    cin >> n;
    Try(1);
    return 0;
}
