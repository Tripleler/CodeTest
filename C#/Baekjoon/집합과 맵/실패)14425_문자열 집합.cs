//https://www.acmicpc.net/problem/14425

//using var sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
//int[] n = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
//var hs = new HashSet<string>();
//for (int i = 0; i < n[0]; i++) hs.Add(sr.ReadLine());
//int cnt = 0;
//for (int j = 0; j < n[1]; j++) if (hs.Contains(sr.ReadLine())) cnt++;
//Console.WriteLine(cnt);

using var sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
int[] n = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
var dic = new Dictionary<string, bool>();
for (int i = 0; i < n[0]; i++) dic[sr.ReadLine()] = true;
int cnt = 0;
for (int j = 0; j < n[1]; j++) if (dic.ContainsKey(sr.ReadLine())) cnt++;
Console.Write(cnt);