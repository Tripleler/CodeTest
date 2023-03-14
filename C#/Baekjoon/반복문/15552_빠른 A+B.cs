//https://www.acmicpc.net/problem/15552
using System.Text;

StringBuilder sb = new StringBuilder();
int n = int.Parse(Console.ReadLine());
for (; n > 0; n--)
{
    sb.AppendLine($"{Array.ConvertAll(Console.ReadLine().Split(), int.Parse).Sum()}");
}
Console.WriteLine(sb);