//https://www.acmicpc.net/problem/2581

bool[] p = new bool[10001];
p[0] = true;
p[1] = true;
for (int i = 2; i < 10001; i++)
{
    if (p[i] == false)
    {
        for (int j = i; j * i < 10001; j++)
        {
            p[j * i] = true;
        }
    }
}

int n = int.Parse(Console.ReadLine());
int m = int.Parse(Console.ReadLine());
int sum = 0, min = 0;
for (int i = m; i >= n; i--)
{
    if (p[i] == false)
    {
        min = i;
        sum += i;
    }
}
Console.Write(min != 0 ? $"{sum}\n{min}" : -1);