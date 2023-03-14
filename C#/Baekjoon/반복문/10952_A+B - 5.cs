//https://www.acmicpc.net/problem/10952
using System.Text;

StringBuilder sb = new StringBuilder();
while (true)
{
    int n = Array.ConvertAll(Console.ReadLine().Split(), int.Parse).Sum();
    if (n == 0) break;
    sb.AppendLine($"{n}");
}
Console.WriteLine(sb);