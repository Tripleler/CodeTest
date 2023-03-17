//https://www.acmicpc.net/problem/10809

int[] a = new int[26];
for (int i = 0; i < 26; i++) a[i] = -1;
string s = Console.ReadLine();
int cnt = 0;
foreach (char c in s)
{
    if (a[c - 97] == -1)
    {
        a[c - 97] = cnt;
    }
    cnt++;
}
Console.Write(string.Join(" ", a));

//string s = Console.ReadLine();
//for (char c = 'a'; c < '{'; c++)
//{
//    Console.Write(s.IndexOf(c) + " ");  // Indexof 없으면 -1 반환
//}