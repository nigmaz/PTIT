#include <bits/stdc++.h>
using namespace std;
int x[30];		  // lưu tập cấu hình chọn xem cho người nào thuê với 0 và 1
int thue[30][30]; // ma trận biểu thị ứng với người thứ i thì thuê những ngày nào - cũng là ma trận biểu thị 0 và 1
int m, n;		  // m là số người thuê và n là số ngày thuê
int giatri = 0;	  // số ngày cho thuê lớn nhất
int kq[30];		  // mảng lưu cấu hình chọn số ngày cho thuê là nhiều nhất
int check[30];	  // mảng kiểm tra xem liệu số ngày cho thuê của người i vs j có trùng nhau không nếu trùng thì hủy chọn người thứ i

void xuly()
{
	for (int i = 1; i <= n; i++)
		check[i] = 0; // Mảng đánh dấu vị trí nào đã cho thuê rồi
	int temp = 0;
	for (int i = 1; i <= m; i++)
	{
		if (x[i] == 1)
		{
			for (int j = 1; j <= n; j++)
			{
				if (check[j] == 1 && thue[i][j] == 1)
					return; // nếu vị trí đó đã cho thuê rồi mà bị trùng vs ng khác thì hủy bỏ phương án
				else if (thue[i][j] == 1 && check[j] == 0)
				{
					temp++;
					check[j] = 1;
				}
			}
		}
	}
	if (temp > giatri)
	{
		// cập nhật kết quả
		giatri = temp;
		for (int i = 1; i <= m; i++)
			kq[i] = x[i];
	}
}

void Try(int i)
{
	// sinh xâu nhị phân độ dài m , 0 là k đồng ý cho người tại vị trí đó thuê máy, 1 là ngược lại
	for (int j = 0; j <= 1; j++)
	{
		x[i] = j;
		if (i == m)
			xuly();
		else
			Try(i + 1);
	}
}

int main()
{
	cout << "So nguoi thue may: ";
	cin >> m;
	cout << "So ngay cho thue may: ";
	cin >> n;
	cout << "Ma tran bieu thi nguoi i thue may vao nhung ngay nao:" << endl;
	for (int i = 1; i <= m; i++)
		for (int j = 1; j <= n; j++)
			cin >> thue[i][j];
	Try(1);
	cout << "So ngay cho thue nhieu nhat: " << giatri << endl;
	cout << "Phuong an cho thue may:" << endl;
	for (int i = 1; i <= m; i++)
		cout << kq[i] << " ";
	return 0;
}

