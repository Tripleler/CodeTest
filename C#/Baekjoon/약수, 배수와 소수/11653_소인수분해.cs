//https://www.acmicpc.net/problem/11653

int n = int.Parse(Console.ReadLine());
if (n == 1) return;
for (int i = 2;i <= n; i++)
{
    while (n % i == 0)
    {
        Console.WriteLine(i);
        n /= i;
    }
}