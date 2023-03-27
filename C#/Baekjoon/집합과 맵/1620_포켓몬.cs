//https://www.acmicpc.net/problem/1620

using var sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
using var sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));
int[] n = Array.ConvertAll(sr.ReadLine().Split(), int.Parse);
var dic = new Dictionary<string, int>();
string[] stack = new string[n[0] + 1];
for (int i = 1; i <= n[0]; i++)
{
    string name = sr.ReadLine();
    dic.Add(name, i);
    stack[i] = name;
}
int id;
for (int j = 1; j <= n[1]; j++)
{
    string s = sr.ReadLine();
    sw.WriteLine(int.TryParse(s, out id) ? stack[id] : dic[s]);
}

//using var sr = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
//using var sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));
//int[] n = Array.ConvertAll(sr.ReadLine().Split(), int.Parse);
//var dic = new Dictionary<string, string>();
//string name, id;
//for (int i = 1; i <= n[0]; i++)
//{
//    id = i.ToString();
//    name = sr.ReadLine();
//    dic.Add(name, id);
//    dic.Add(id, name);
//}
//for (int j = 1; j <= n[1]; j++) sw.WriteLine(dic[sr.ReadLine()]);