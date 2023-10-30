#include <bits/stdc++.h>
using namespace std;
int x[30];            // Lưu tập cấu hình ứng với công việc v thứ i thì chọn giải quyết công việc ý ở quá trình thứ nào
int cv[30][30];       // ma trận biểu thị ứng với công việc v thứ i thì ở quá trình n mất bao nhiêu thời gian
int n;                // số quá trình = số công việc
int check[30];        // để kiểm tra xem nếu việc v i đã được xử lý ở quá trình n 1 thì quá trình n1 không được lặp lại
int giatri = INT_MAX; // hàm lưu thời gian tối ưu
int kq[30];           // hàm lưu kết quả với thời gian tối ưu

void xuly()
{
    // cập nhật kết quả
    int temp = 0;
    for (int i = 1; i <= n; i++)
    {
        temp += cv[x[i]][i];
    }
    if (temp < giatri)
    {
        giatri = temp;
        for (int i = 1; i <= n; i++)
            kq[i] = x[i];
    }
}

void Try(int i)
{
    // coi công việc thứ i được giao cho việc j thực hiện, sinh các hoán vị việc j
    for (int j = 1; j <= n; j++)
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
    cout << "So qua trinh: ";
    cin >> n;
    cout << "Ma tran bieu thi thoi gian xu li cong viec v tai qua trinh n:" << endl;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            cin >> cv[i][j];
    Try(1);
    cout << "Gia tri toi uu la: " << giatri << "\nLua chon toi uu la: "; // thời gian min
    for (int i = 1; i <= n; i++)
        cout << kq[i] << " ";
    return 0;
}
