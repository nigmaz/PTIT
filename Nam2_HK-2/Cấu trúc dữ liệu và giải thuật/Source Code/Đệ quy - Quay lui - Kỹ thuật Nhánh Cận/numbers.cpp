#include <iostream>
using namespace std;
int n, A[20];

void output(int m)
{
    for (int i = 1; i <= m; i++)
        cout << A[i] << " ";
    cout << endl;
}

void Try(int i, int j, int s)
{
    for (int k = j; k > 0; k--)
    {
        if (s + k <= n)
        {
            A[i] = k;
            s += k;
            if (s == n)
                output(i);
            else
                Try(i + 1, k, s);
            s -= k;
        }
    }
}

int main()
{
    cin >> n;
    Try(1, n, 0);
    return 0;
}
