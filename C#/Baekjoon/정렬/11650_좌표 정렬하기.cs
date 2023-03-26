//https://www.acmicpc.net/problem/11650

using StreamReader sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
using StreamWriter sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));
var list = new List<Tuple<int, int>>();
int n = int.Parse(sr.ReadLine());
for (int i = 0; i < n; i++)
{
    int[] c = Array.ConvertAll(sr.ReadLine().Split(), int.Parse);
    list.Add(new Tuple<int, int>(c[0], c[1]));
}
list.Sort();
foreach (var e in list) sw.WriteLine($"{e.Item1} {e.Item2}");


//using StreamReader sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
//using StreamWriter sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));
//int n = int.Parse(sr.ReadLine());
//var C = new (int x, int y)[n];
//for (int i = 0; i < n; i++)
//{
//    var c = Array.ConvertAll(sr.ReadLine().Split(), int.Parse);
//    C[i] = (c[0], c[1]);
//}
//Array.Sort(C);
//foreach (var c in C) sw.WriteLine($"{c.x} {c.y}");