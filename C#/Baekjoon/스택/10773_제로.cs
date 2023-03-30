//https://www.acmicpc.net/problem/10773

using var sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
var s = new Stack<int>();
int n = int.Parse(sr.ReadLine()), p;
while (n-- > 0)
{
    p = int.Parse(sr.ReadLine());
    if (p == 0) s.Pop();
    else s.Push(p);
}
Console.Write(s.Sum());