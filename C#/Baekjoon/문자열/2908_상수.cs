//https://www.acmicpc.net/problem/2908

string[] s = Console.ReadLine().Split();
int n1 = int.Parse(s[0].Reverse().ToArray());
int n2 = int.Parse(s[1].Reverse().ToArray());
Console.Write(Math.Max(n1, n2));