////https://www.acmicpc.net/problem/11651

using StreamReader sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
using StreamWriter sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));
int n = int.Parse(sr.ReadLine());
var C = new (int x, int y)[n];
for (int i = 0; i < n; i++)
{
    var c = Array.ConvertAll(sr.ReadLine().Split(), int.Parse);
    C[i] = (c[0], c[1]);
}
foreach (var c in C.OrderBy(k => k.y).ThenBy(k => k.x).ToArray()) sw.WriteLine($"{c.x} {c.y}");

//using var sw = new StreamWriter(Console.OpenStandardOutput());

//var n = int.Parse(Console.ReadLine());
//var C = new (int x, int y)[n];

//for (int i = 0; i < n; i++)
//{
//    var c = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
//    C[i] = (c[1], c[0]);  // 여기서 뒤집음
//}

//Array.Sort(C);

//foreach (var c in C) sw.WriteLine(c.y + " " + c.x);