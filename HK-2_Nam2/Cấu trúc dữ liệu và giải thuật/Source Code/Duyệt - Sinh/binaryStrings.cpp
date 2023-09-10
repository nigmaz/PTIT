#include <iostream>
using namespace std;
int n, B[20];
bool check;

void output()
{
    for (int i = 1; i <= n; i++)
        cout << B[i] << " ";
    cout << endl;
}

void sinhketiep()
{
    int i = n;
    while (B[i] == 1)
    {
        B[i] = 0;
        i--;
    }
    if (i == 0)
        check = true;
    else
        B[i] = 1;
}

int main()
{
    cin >> n;
    while (!check)
    {
        output();
        sinhketiep();
    }
    return 0;
}
