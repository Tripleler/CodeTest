//https://www.acmicpc.net/problem/1764

using var sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));
int[] n = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
var A = new HashSet<string>();
var B = new HashSet<string>();
for (int i = 0; i < n[0]; i++) A.Add(Console.ReadLine());
for (int j = 0; j < n[1]; j++) B.Add(Console.ReadLine());
A.IntersectWith(B);
string[] s = A.ToArray();
Array.Sort(s);
sw.WriteLine(s.Length);
foreach (string s2 in s) sw.WriteLine(s2);