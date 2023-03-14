//https://www.acmicpc.net/problem/11022
int n = int.Parse(Console.ReadLine());
for (int i = 1; i <= n; i++)
{
    int[] s = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
    Console.WriteLine($"Case #{i}: {s[0]} + {s[1]} = {s[0] + s[1]}");
}