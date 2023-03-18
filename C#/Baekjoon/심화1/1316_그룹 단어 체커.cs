//https://www.acmicpc.net/problem/1316

int n = int.Parse(Console.ReadLine());
int cnt = n;
for (int i = 0; i < n; i++)
{
    bool[] a = new bool[26];
    string s = Console.ReadLine();
    char b = '1';
    foreach (char c in s)
    {
        if (c != b)
        {
            if (a[c - 97] == false)
            {
                a[c - 97] = true;
                b = c;
            }
            else
            {
                cnt -= 1;
                break;
            }                
        }
    }
}
Console.Write(cnt);