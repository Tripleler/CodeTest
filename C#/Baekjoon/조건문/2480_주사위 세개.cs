//https://www.acmicpc.net/problem/2480
int[] n = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
Array.Sort(n);
if (n[0] == n[1] && n[1] == n[2])
{
    Console.WriteLine($"{10000 + 1000 * n[0]}");
}
else if (n[0] != n[1] && n[1] != n[2])
{
    Console.WriteLine($"{100 * n.Max()}");
}
else
{
    Console.WriteLine($"{1000 + 100 * (n[0] == n[1] ? n[0] : n[1])}");
}