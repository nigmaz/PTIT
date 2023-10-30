#include <bits/stdc++.h>
using namespace std;
long n, W;

struct Items
{
    long weight;
    long value;
};

Items A[200];

void Init()
{
    cin >> n >> W;
    for (int i = 0; i < n; i++)
    {
        cin >> A[i].weight;
        cin >> A[i].value;
    }
}

bool cmp(Items a, Items b)
{
    return (float)a.value / a.weight > (float)b.value / b.weight;
    // tỉ lệ value/weight
}

long Try(int i, long w, long val)
{
    if (w > W)
        return 0;
    if (i == n && w <= W)
        return val;
    long l = Try(i + 1, w + A[i].weight, val + A[i].value);
    long r = Try(i + 1, w, val);
    return max(l, r);
}

int main()
{
    Init();
    sort(A, A + n, cmp);
    cout << Try(0, 0, 0) << endl;
    return 0;
}
