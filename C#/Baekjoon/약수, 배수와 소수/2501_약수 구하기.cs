//https://www.acmicpc.net/problem/2501

int[] n = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
for (int i = 1; i <= n[0]; i++)
{
    if (n[0] % i == 0) n[1] -= 1;
    if (n[1] == 0)
    {
        Console.Write(i);
        return;
    }
}
Console.Write(0);