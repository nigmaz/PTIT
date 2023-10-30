#include <iostream>
using namespace std;
int n, A[20];
bool check;

void output()
{
    for (int i = 1; i <= n; i++)
        cout << A[i] << " ";
    cout << endl;
}

void sinhketiep()
{
    int i, j, t, d, c;
    i = n - 1;
    while (A[i] > A[i + 1])
        i--;
    if (i == 0)
        check = true;
    else
    {
        j = n;
        while (A[j] < A[i])
            j--;
        t = A[i];
        A[i] = A[j];
        A[j] = t;
        d = i + 1;
        c = n;
        while (d < c)
        {
            t = A[d];
            A[d] = A[c];
            A[c] = t;
            d++;
            c--;
        }
    }
}

int main()
{
    cin >> n;
    for (int i = 1; i <= n; i++)
        A[i] = A[i - 1] + 1;
    while (!check)
    {
        output();
        sinhketiep();
    }
    return 0;
}
