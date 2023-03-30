//https://www.acmicpc.net/problem/9012

using var sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
using var sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));
string t;
int n = int.Parse(sr.ReadLine());
while (n-- > 0)
{
    var s = new Stack<char>();
    char d;
    t = sr.ReadLine();
    foreach (char c in t)
    {
        if (s.TryPeek(out d) && d == '(' && c == ')') s.Pop();
        else s.Push(c);
    }
    sw.WriteLine(s.Count == 0 ? "YES" : "NO");
}