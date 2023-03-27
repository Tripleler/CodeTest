//https://www.acmicpc.net/problem/10815

using System.Text;

var sb = new StringBuilder();
Console.ReadLine();
int[] cards = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
var dic = new Dictionary<int, bool>();
foreach (int card in cards) dic[card] = true;
int n = int.Parse(Console.ReadLine());
int[] check = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
foreach (int c in check) sb.Append(dic.ContainsKey(c) ? "1 " : "0 ");
Console.Write(sb);


// sw 속도가 sb보다 빠름

//using var sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));
//Console.ReadLine();
//int[] cards = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
//var hs = new HashSet<int>(cards);
//int n = int.Parse(Console.ReadLine());
//cards = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
//foreach (int c in cards) sw.Write(hs.Contains(c) ? "1 " : "0 ");