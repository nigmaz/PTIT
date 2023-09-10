#include <iostream>
using namespace std;
int n, C[20];
bool check[20], xuoi[39], nguoc[39];

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
        if (!check[j] && !xuoi[i - j + n] && !nguoc[i + j - 1])
        {
            C[i] = j;
            check[j] = true;
            xuoi[i - j + n] = true;
            nguoc[i + j - 1] = true;
            if (i == n)
                output();
            else
                Try(i + 1);
            check[j] = false;
            xuoi[i - j + n] = false;
            nguoc[i + j - 1] = false;
        }
    }
}

int main()
{
    cin >> n;
    Try(1);
    return 0;
}
