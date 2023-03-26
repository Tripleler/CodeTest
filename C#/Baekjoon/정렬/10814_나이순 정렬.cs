//https://www.acmicpc.net/problem/10814

using var sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
using var sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));
int n = int.Parse(sr.ReadLine());
var S = new (int x, string y)[n];
for (int i = 0; i < n; i++)
{
    var r = sr.ReadLine().Split();
    S[i] = (int.Parse(r[0]), r[1]);
}
foreach (var s in S.OrderBy(k => k.x)) sw.WriteLine($"{s.x} {s.y}");