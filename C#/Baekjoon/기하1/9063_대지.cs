//https://www.acmicpc.net/problem/9063

int n = int.Parse(Console.ReadLine());
int[] x = new int[n];
int[] y = new int[n];
for (int i = 0; i < n; i++)
{
    int[] c = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
    x[i] = c[0];
    y[i] = c[1];
}
Console.Write((x.Max() - x.Min()) * (y.Max() - y.Min()));