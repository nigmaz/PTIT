#include <iostream>
using namespace std;
int n, k, C[20];

void output()
{
    for (int i = 1; i <= k; i++)
        cout << C[i] << " ";
    cout << endl;
}

void Try(int i)
{
    for (int j = C[i - 1] + 1; j <= n - k + i; j++)
    {
        C[i] = j;
        if (i == k)
            output();
        else
            Try(i + 1);
    }
}

int main()
{
    cin >> n >> k;
    Try(1);
    return 0;
}
