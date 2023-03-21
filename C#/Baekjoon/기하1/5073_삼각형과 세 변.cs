//https://www.acmicpc.net/problem/5073

using System.Text;

StringBuilder sb = new StringBuilder();
while (true)
{
    int[] n = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
    if (n[0] == 0) break;
    Array.Sort(n);
    if (n[0] == n[1] && n[1] == n[2]) sb.AppendLine("Equilateral");
    else if (n[0] + n[1] <= n[2]) sb.AppendLine("Invalid");
    else if (n[0] == n[1] || n[1] == n[2]) sb.AppendLine("Isosceles");
    else sb.AppendLine("Scalene");
}
Console.Write(sb);