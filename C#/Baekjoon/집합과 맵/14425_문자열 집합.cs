//https://www.acmicpc.net/problem/14425

int[] n = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
int cnt = 0;
var S = new HashSet<string>();
while (n[0]-- > 0) S.Add(Console.ReadLine());
while (n[1]-- > 0) if (S.Contains(Console.ReadLine())) cnt++;
Console.Write(cnt);