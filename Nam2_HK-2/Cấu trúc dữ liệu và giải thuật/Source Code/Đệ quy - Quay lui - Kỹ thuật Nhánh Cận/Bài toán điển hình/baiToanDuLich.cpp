// The Traveling Salesman Problem (TSP)
// Duyệt toàn bộ
#include <bits/stdc++.h>
using namespace std;
int x[30];            // tập phương án chọn đường đi
int dulich[30][30];   // tập ma trận chi phí
int n;                // số thành phố cần đi qua
int check[30];        // tập kiểm tra xem thành phố đó đã đi qua chưa để không chọn trùng
int giatri = INT_MAX; // chi phí thấp nhất sẽ được gán vào biến này
int kq[30];           // tập chọn phương án tối ưu lưu ở đây

void xuly()
{
    // cập nhật giá trị kết quả khi đã sinh đủ tất cả thành phố
    int temp = dulich[1][x[2]];
    for (int i = 2; i < n; i++)
    {
        temp += dulich[x[i]][x[i + 1]];
    }
    temp += dulich[x[n]][1];
    if (temp < giatri)
    {
        giatri = temp;
        kq[1] = 1; // TP đầu tiên là TP 1
        for (int i = 2; i <= n; i++)
            kq[i] = x[i];
        kq[n + 1] = 1; // TP cuối cùng là TP đầu tiên
    }
}

void Try(int i)
{
    // Quay lui hoán vị từ thành phố thứ 2 đến thành phố cuối cùng
    for (int j = 2; j <= n; j++)
    {
        if (check[j] == 0)
        {
            x[i] = j;
            check[j] = 1;
            if (i == n)
            {
                xuly();
            }
            else
                Try(i + 1);
            check[j] = 0;
        }
    }
}

int main()
{
    cout << "So thanh pho di qua: ";
    cin >> n;
    cout << "Ma tran bieu dien chi phi tu TP i -> TP j:" << endl;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            cin >> dulich[i][j];
    // chọn TP 1 là điểm xuất phát
    Try(2);
    cout << "Gia tri toi uu la: " << giatri << "\nLua chon toi uu la: ";
    for (int i = 1; i <= n + 1; i++)
        cout << kq[i] << " ";
    return 0;
}
