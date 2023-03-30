//https://www.acmicpc.net/problem/10828

using var sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
using var sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));
Stack<int> s = new Stack<int>();
string l;
int n = int.Parse(sr.ReadLine()), i;
while (n-- > 0)
{
    l = sr.ReadLine();
    if (l == "pop") sw.WriteLine(s.TryPop(out i) ? i : -1);
    else if (l == "size") sw.WriteLine(s.Count);
    else if (l == "empty") sw.WriteLine(s.Count == 0 ? 1 : 0);
    else if (l == "top") sw.WriteLine(s.Count == 0 ? -1 : s.Peek());
    else s.Push(int.Parse(l.Split()[1]));
}