//https://www.acmicpc.net/problem/2108

StreamReader sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
int n = int.Parse(sr.ReadLine());
int[] a = new int[n];
int[] b = new int[8001];
for (int i = 0; i < n; i++)
{
    int c = int.Parse(sr.ReadLine());
    a[i] = c;
    b[c + 4000]++;
}
Array.Sort(a);
Console.WriteLine((int)Math.Round(a.Average()));
Console.WriteLine(a[n / 2]);
int[] f = Array.FindAll(b, e => e == b.Max());
int m = Array.IndexOf(b, f[0]);
if (f.Length == 1) Console.WriteLine(m - 4000);
else
{
    b[m] = 0;
    Console.WriteLine(Array.IndexOf(b, f[0]) - 4000);
}
Console.WriteLine(a.Max() - a.Min());
sr.Close();