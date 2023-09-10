#include <iostream>
using namespace std;

int binarySearch(int A[], int value, int left, int right)
{
    while (left <= right)
    {
        int midle = (left + right) / 2;
        if (A[midle] == value)
            return midle;
        else if (A[midle] > value)
            right = midle - 1;
        else
            left = midle + 1;
    }
    return -1;
}

int main()
{
    int n, x;
    cin >> n >> x;
    int A[100];
    for (int i = 0; i < n; i++)
        cin >> A[i];
    cout << binarySearch(A, x, 0, n - 1);
    return 0;
}
