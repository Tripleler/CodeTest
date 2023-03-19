//https://www.acmicpc.net/problem/2563

bool[,] paper = new bool[100, 100];
int n = int.Parse(Console.ReadLine());
int cnt = 0;
for (int i = 0; i < n; i++)
{
    int[] c = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
    for (int x = c[0]; x < c[0] + 10; x++)
    {
        for (int y = c[1]; y < c[1] + 10; y++)
        {
            if (paper[x, y] == false)
            {
                paper[x, y] = true;
                cnt += 1;
            }
        }
    }
}
Console.Write(cnt);