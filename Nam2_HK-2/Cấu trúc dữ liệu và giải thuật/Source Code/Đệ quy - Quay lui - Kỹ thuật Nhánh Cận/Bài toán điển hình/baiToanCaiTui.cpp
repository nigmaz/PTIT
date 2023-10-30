// Duyệt toàn bộ
#include <iostream>
using namespace std;
int x[100];    // tập x là cấu hình lựa chọn đồ vật thỏa mãn nhỏ hơn khối lượng tối đa b;
int a[100];    // trọng lượng của đồ vật thứ i là ai;
int c[100];    // giá trị sử dụng của đồ vật thứ i là ci;
int n, b;      // n là số đồ vật, b là khối lượng tối đa của túi
int xopt[100]; // mảng lưu cấu hình lựa chọn thỏa mãn (tối ưu nhất về giá trị sử dụng)
int fopt;      // giá trị sử dụng tối ưu nhất

void init()
{
    cout << "so do vat:";
    cin >> n;
    cout << "trong luong toi da:";
    cin >> b;
    cout << "trong luong tung do vat: ";
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
    }
    cout << "gia tri tung do vat:";
    for (int i = 1; i <= n; i++)
    {
        cin >> c[i];
    }
}

bool check_weight()
{
    int weight = 0;
    for (int i = 1; i <= n; i++)
    {
        weight += a[i] * x[i];
    }

    if (weight > b)
    {
        return false;
    }
    return true;
}

void sum_up()
{
    int sum = 0;
    for (int i = 1; i <= n; i++)
    {
        sum += x[i] * c[i];
    }
    if (fopt < sum)
    {
        fopt = sum;
        for (int i = 1; i <= n; i++)
        {
            xopt[i] = x[i];
        }
    }
}

void Try(int i)
{
    for (int j = 0; j <= 1; j++)
    {
        x[i] = j;
        if (i == n)
        {
            if (check_weight())
            {

                sum_up();
            }
        }
        else
            Try(i + 1);
    }
}

void result()
{
    cout << "gia tri su dung toi uu:" << endl
         << fopt << endl;
    cout << "phuong an toi uu: " << endl;
    for (int i = 1; i <= n; i++)
    {
        cout << xopt[i] << " ";
    }
}

int main()
{
    init();
    Try(1);
    result();
    return 0;
}
