//https://www.acmicpc.net/problem/2941

string s = Console.ReadLine();
string[] a = new string[8] { "c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=" };
foreach (string c in a)
{
    s = s.Replace(c, "1");
}
Console.WriteLine(s.Length);