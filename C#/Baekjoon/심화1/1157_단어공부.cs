//https://www.acmicpc.net/problem/1157

int[] a = new int[26];
string s = Console.ReadLine().ToLower();
foreach (char c in s)
{
    a[c - 97] += 1;
}
int left = Array.IndexOf(a, a.Max());
Console.Write(left == Array.LastIndexOf(a, a.Max()) ? $"{(char)(left + 65)}" : "?");

//int[] a = new int[26];
//string s = Console.ReadLine().ToLower();
//foreach (char c in s)
//{
//    a[c - 97] += 1;
//}
//Console.Write(Array.FindAll(a, x => x == a.Max()).Length == 1 ? $"{(char)(Array.IndexOf(a, a.Max()) + 65)}" : "?");