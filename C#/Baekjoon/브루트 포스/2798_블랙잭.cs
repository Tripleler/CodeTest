//https://www.acmicpc.net/problem/2798

int[] n = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
int[] c = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
int m = 0;
for (int i = 0; i < n[0] - 2; i++)
{
    for (int j = i + 1; j < n[0] - 1; j++)
    {
        for (int k = j + 1; k < n[0]; k++)
        {
            int s = c[i] + c[j] + c[k];
            if (s <= n[1]) m = Math.Max(m, s);
        }
    }
}
Console.Write(m);