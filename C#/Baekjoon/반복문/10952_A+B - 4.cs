//https://www.acmicpc.net/problem/10951
using System.Text;

StringBuilder sb = new StringBuilder();
while (true)
{
    string s = Console.ReadLine();
    if (s == null) break;
    string[] t = s.Split();
    sb.AppendLine($"{Array.ConvertAll(t, int.Parse).Sum()}");
}
Console.WriteLine(sb);

// 실행하면 에러나는데 테케는 통과함 왜지??