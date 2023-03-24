//https://www.acmicpc.net/problem/2750

int n = int.Parse(Console.ReadLine());
int[] a = new int[n];
for (int i = 0; i < n; i++)
{
    a[i] = int.Parse(Console.ReadLine());
}
Array.Sort(a);
Console.Write(string.Join('\n', a));