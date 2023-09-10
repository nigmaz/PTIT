#include <iostream>
using namespace std;

void quickSort(int A[], int left, int right)
{
    int i = left, j = right;
    int tmp;
    int pivot = A[(left + right) / 2];
    while (i <= j)
    {
        while (A[i] < pivot)
            i++;
        while (A[j] > pivot)
            j--;
        if (i <= j)
        {
            tmp = A[i];
            A[i] = A[j];
            A[j] = tmp;
            i++;
            j--;
        }
    }

    if (left < j)
        quickSort(A, left, j);
    if (i < right)
        quickSort(A, i, right);
}

int main()
{
    int n;
    cin >> n;
    int A[100];
    for (int i = 0; i < n; i++)
        cin >> A[i];
    quickSort(A, 0, n - 1);
    for (int i = 0; i < n; i++)
        cout << A[i] << " ";
    return 0;
}
