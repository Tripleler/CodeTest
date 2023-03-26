//https://www.acmicpc.net/problem/1181

using var sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
using var sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));
int n = int.Parse(sr.ReadLine());
var S = new string[n];
for (int i = 0; i < n; i++)
{
    S[i] = sr.ReadLine();
}
foreach (var s in S.Distinct().OrderBy(x => x.Length).ThenBy(x => x)) sw.WriteLine(s);