#include <iostream>
using namespace std;

int main()
{
	int n;
	cin >> n;
	int A[100];
	for (int i = 0; i < n; i++)
		cin >> A[i];
	int min_idx;
	for (int i = 0; i < n - 1; i++)
	{
		min_idx = i;
		for (int j = i + 1; j < n; j++)
		{
			if (A[min_idx] > A[j])
				min_idx = j;
		}
		if (min_idx != i)
		{
			int tmp = A[min_idx];
			A[min_idx] = A[i];
			A[i] = tmp;
		}
	}
	for (int i = 0; i < n; i++)
		cout << A[i] << " ";
	cout << endl;
	return 0;
}

