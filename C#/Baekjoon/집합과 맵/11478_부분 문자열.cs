//https://www.acmicpc.net/problem/11478

var hs = new HashSet<string>();
string s = Console.ReadLine();
int n = s.Length;
for (int i = 1; i <= n; i++)  //개수
{
    for (int j = 0; j <= n - i; j++)  // 위치
    {
        hs.Add(s.Substring(j, i));
    }
}
Console.WriteLine(hs.Count);