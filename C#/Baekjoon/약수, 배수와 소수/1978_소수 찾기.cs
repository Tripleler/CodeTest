//https://www.acmicpc.net/problem/1978

bool[] p = new bool[1001];
p[0] = true;
p[1] = true;
for (int i = 2; i < 1001; i++)
{
    if (p[i] == false)
    {
        for (int j = i; j * i < 1001; j++)
        {
            p[j * i] = true;
        }
    }
}
Console.ReadLine();
int[] n = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
int cnt = 0;
foreach (int i in n)
{
    if (p[i] == false) cnt++;
}
Console.Write(cnt);