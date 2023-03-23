//https://www.acmicpc.net/problem/24313

int[] a = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
int c = int.Parse(Console.ReadLine());
int n = int.Parse(Console.ReadLine());
Console.Write(a[0] * n + a[1] <= c * n && c >= a[0] ? "1" : "0");