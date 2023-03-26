//https://www.acmicpc.net/problem/18870

using System.Text;

var sb = new StringBuilder();
int n = int.Parse(Console.ReadLine());
int[] C = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
int[] S = C.Distinct().OrderBy(x => x).ToArray();
var D = new Dictionary<int, int>();
for (int i = 0; i < S.Length; i++) D[S[i]] = i;
foreach (int c in C) sb.Append($"{D[c]} ");
Console.Write(sb);