//https://www.acmicpc.net/problem/18258

using System.Text;

using var sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
using var sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));
var sb = new StringBuilder();
var q = new Queue<int>();
int n = int.Parse(sr.ReadLine());
string s, last = "";
while (n-- > 0)
{
    s = sr.ReadLine();
    if (s.Contains(' '))
    {
        last = s.Split()[1];
        q.Enqueue(int.Parse(last));
    }
    else if (s == "pop") sb.AppendLine(q.Count == 0 ? "-1" : $"{q.Dequeue()}");
    else if (s == "size") sb.AppendLine($"{q.Count}");
    else if (s == "empty") sb.AppendLine(q.Count == 0 ? "1" : "0");
    else if (s == "front") sb.AppendLine(q.Count == 0 ? "-1" : $"{q.Peek()}");
    else if (s == "back") sb.AppendLine(q.Count == 0 ? "-1" : last);
}
sw.Write(sb);