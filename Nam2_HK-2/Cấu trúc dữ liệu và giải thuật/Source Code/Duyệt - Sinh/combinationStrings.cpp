#include <iostream>
using namespace std;
int n, k, C[20];
bool check;

void output()
{
    for (int i = 1; i <= k; i++)
        cout << C[i] << " ";
    cout << endl;
}

void sinhketiep()
{
    int i = k;
    while (C[i] == n - k + i)
        i--;
    if (i == 0)
        check = true;
    else
    {
        C[i]++;
        for (int j = i + 1; j <= k; j++)
            C[j] = C[j - 1] + 1;
    }
}

int main()
{
    cin >> n >> k;
    for (int i = 1; i <= k; i++)
        C[i] = C[i - 1] + 1;
    while (!check)
    {
        output();
        sinhketiep();
    }
    return 0;
}
