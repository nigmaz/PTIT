#include <iostream>
using namespace std;

int main()
{
	int n;
	cin >> n;
	int A[100];
	for (int i = 0; i < n; i++)
		cin >> A[i];
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n - i; j++)
		{
			if (A[j] > A[j + 1])
			{
				int tmp = A[j];
				A[j] = A[j + 1];
				A[j + 1] = tmp;
			}
		}
	}
	for (int i = 0; i < n; i++)
		cout << A[i] << " ";
	cout << endl;
	return 0;
}
