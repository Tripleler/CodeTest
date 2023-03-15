//https://www.acmicpc.net/problem/10871
using System.Text;

int n = int.Parse(Console.ReadLine().Split()[1]);
int[] nums = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
StringBuilder sb = new StringBuilder();
foreach (int i in nums)
{
    if (i < n) sb.Append($"{i} ");
}
Console.WriteLine(sb);

//int[] nx = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
//int[] aa = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

//Console.Write(String.Join(' ', aa.Where(a => a < nx[1])));