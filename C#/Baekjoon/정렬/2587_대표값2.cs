//https://www.acmicpc.net/problem/2587

int[] a = new int[5];
for (int i = 0; i < 5; i++)
{
    a[i] = int.Parse(Console.ReadLine());
}
Array.Sort(a);
Console.Write($"{a.Average()}\n{a[2]}");