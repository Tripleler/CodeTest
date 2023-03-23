//https://www.acmicpc.net/problem/1018

int[] s = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
bool[,] b = new bool[s[0], s[1]];
for (int i = 0; i < s[0]; i++)
{
    string r = Console.ReadLine();
    for (int j = 0; j < s[1]; j++)
    {
        b[i, j] = r[j] == 'B';
    }
}

int m = 64;
for (int r = 0; r < s[0] - 7; r++) for (int c = 0; c < s[1] - 7; c++)
    {
        int n = 0;
        for (int i = r; i < r + 8; i++) for (int j = c; j < c + 8; j++)
            {
                if (b[i, j] ^ (i - r + j - c) % 2 == 0) n++;
            }
        m = Math.Min(m, Math.Min(n, 64 - n));
    }
Console.Write(m);