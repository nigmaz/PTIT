#include <bits/stdc++.h>
using namespace std;
long n, A[100];
bool check[20];
long c[20][20];
long MIN = 1e9, cmin = 1e9;
long s = 0;

void Init()
{
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            cin >> c[i][j];
            cmin = min(cmin, c[i][j]);
        }
    }
}

void Try(int i)
{
    if (s + cmin * (n - i + 1) >= MIN)
        return;
    for (int j = 2; j <= n; j++)
    {
        if (!check[j])
        {
            A[i] = j;
            check[j] = true;
            s += c[A[i - 1]][j];
            if (i == n)
            {
                if (s + c[A[n]][A[1]] < MIN)
                    MIN = s + c[A[n]][A[1]];
            }
            else
                Try(i + 1);
            s -= c[A[i - 1]][j];
            check[j] = false;
        }
    }
}

int main()
{
    check[1] = true;
    A[1] = 1;
    Init();
    Try(2);
    cout << MIN << endl;
    return 0;
}
