//https://www.acmicpc.net/problem/4949

using System.Text.RegularExpressions;

using var sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
using var sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));
string l;
char m;
while (true)
{
    var s = new Stack<char>();
    l = sr.ReadLine();
    if (l == ".") break;
    l = Regex.Replace(l, @"[^\[\]()]", "");
    foreach (char c in l)
    {
        if (s.TryPeek(out m) && (m == '(' && c == ')' || m == '[' && c == ']')) s.Pop();
        else s.Push(c);
    }
    sw.WriteLine(s.Count == 0 ? "yes" : "no");
}