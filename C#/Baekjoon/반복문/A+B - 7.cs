//https://www.acmicpc.net/problem/11021
int n = int.Parse(Console.ReadLine());
for (int i = 1; i <= n; i++)
{
    Console.WriteLine($"Case #{i}: {Array.ConvertAll(Console.ReadLine().Split(), int.Parse).Sum()}");
}