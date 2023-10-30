#include <iostream>
using namespace std;
int n, C[20];
bool check[20];

void output()
{
    for (int i = 1; i <= n; i++)
        cout << C[i] << " ";
    cout << endl;
}

void Try(int i)
{
    for (int j = 1; j <= n; j++)
    {
        if (!check[j])
        {
            C[i] = j;
            check[j] = true;
            if (i == n)
                output();
            else
                Try(i + 1);
            check[j] = false;
        }
    }
}

int main()
{
    cin >> n;
    Try(1);
    return 0;
}
