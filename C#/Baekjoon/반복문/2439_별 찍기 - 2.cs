//https://www.acmicpc.net/problem/2439
using System.Text;

int n = int.Parse(Console.ReadLine());
StringBuilder sb = new StringBuilder();
for (int i = 1; i <= n; i++)
{
    for (int j = 0; j < n - i; j++)
    {
        sb.Append(" ");
    }
    for (int j = 0; j < i; j++)
    {
        sb.Append("*");
    }
    sb.Append("\n");
}
Console.WriteLine(sb.ToString());