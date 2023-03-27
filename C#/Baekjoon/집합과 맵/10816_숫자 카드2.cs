//https://www.acmicpc.net/problem/10816

using var sw = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));
Console.ReadLine();
string[] cards = Console.ReadLine().Split();
var dic = new Dictionary<string, int>();
int n;
foreach (string card in cards)
{
    if (dic.TryGetValue(card, out n)) dic[card] = n + 1;
    else dic[card] = 1;
}
Console.ReadLine();
cards = Console.ReadLine().Split();
foreach (string card in cards) sw.Write(dic.TryGetValue(card, out n) ? $"{n} " : "0 ");